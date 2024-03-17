import argparse
import os
import socket
import ssl
import sys
import cgi

CERT = 'cert.pem'
KEY = 'key.pem'

if sys.version_info.major == 2:
    import SimpleHTTPServer as http_server
    import SocketServer as socket_server
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
    SSL_PROTOCOL = ssl.PROTOCOL_SSLv23
else:
    import http.server as http_server
    import socketserver as socket_server
    from http.server import HTTPServer, BaseHTTPRequestHandler
    SSL_PROTOCOL = ssl.PROTOCOL_TLS_SERVER

class HTTPRequestHandler(http_server.SimpleHTTPRequestHandler):

    def do_PUT(self):
        path = self.translate_path(self.path)
        if path.endswith('/'):
            self.send_response(405, "Method Not Allowed")
            self.wfile.write("PUT not allowed on a directory\n".encode())
            return
        else:
            try:
                os.makedirs(os.path.dirname(path))
            except OSError:
                pass
            if os.path.exists(path):
                # File already exists, find the next available filename
                base_path, extension = os.path.splitext(path)
                i = 1
                while os.path.exists("{0}_{1}{2}".format(base_path, i, extension)):
                    i += 1
                new_path = "{0}_{1}{2}".format(base_path, i, extension)
                path = new_path

            length = int(self.headers['Content-Length'])
            with open(path, 'wb') as f:
                f.write(self.rfile.read(length))
            self.send_response(201, "Created")
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("File Putting Successfully\n".encode())



    def do_POST(self):
        # Handle the POST request here
        content_type, params = cgi.parse_header(self.headers.get('Content-Type'))

        # Check if it's a multipart/form-data POST request
        if content_type == 'multipart/form-data':
            try:
                # Parse the form data to get the file content
                form_data = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type']}
                )

                # Check if 'file' field exists in the form data
                if 'file' in form_data:
                    file_item = form_data['file']
                    original_filename = file_item.filename  # Get the original filename

                    # Check if the file already exists
                    counter = 1
                    base_name, extension = os.path.splitext(original_filename)
                    while os.path.exists(original_filename):
                        original_filename = f"{base_name}_{counter}{extension}"
                        counter += 1

                    # Save the file content to a file with the unique filename
                    with open(original_filename, 'wb') as file:
                        file.write(file_item.file.read())

                    # Process the file content as needed
                    print("Received file content and saved as:", original_filename)

                    # Send a response back to the client
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(f"File '{original_filename}' received and processed successfully\n".encode())
                    return

            except Exception as e:
                print("Error processing form data:", str(e))

        # If the request does not match the expected format, send a 400 Bad Request response
        self.send_response(400)  # Bad Request
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("Invalid form data format\n".encode())


    def do_DELETE(self):
        path = self.translate_path(self.path)
        if os.path.exists(path):
            try:
                os.remove(path)
                self.send_response(200, "OK")
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write("File Deleted Successfully\n".encode())
            except Exception as e:
                self.send_response(500, "Internal Server Error")
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write("Error Deleting File: {}\n".format(str(e)).encode())
        else:
            self.send_response(404, "Not Found")
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("File Not Found\n".encode())


class SecureHTTPServer(socket_server.ThreadingMixIn, HTTPServer):
    def __init__(self, server_address, HandlerClass):
        try:
            HTTPServer.__init__(self, server_address, HandlerClass)

            # Create an SSLContext and load the certificate and key
            ctx = ssl.SSLContext(SSL_PROTOCOL)
            ctx.load_cert_chain(certfile=CERT, keyfile=KEY)

            # Wrap the socket with the SSLContext
            self.socket = ctx.wrap_socket(socket.socket(self.address_family, self.socket_type),
                                         server_side=True)

            self.server_bind()
            self.server_activate()
        except Exception as e:
            print("\033[1;31mError: {}\033[0m".format(e))
            sys.exit(1)

    def server_close(self):
        self.socket.close()
        HTTPServer.server_close(self)

# Banner printing function
def print_banner():
    print("\033[0m")
    print("\033[1;34m                    ___           __              __    ")
    print("\033[1;34m    ________ __  __| _/_______  _|__|__  __ ____ |  | __")
    print("\033[1;34m   /  ___/  |  \/ __ |/  _ \  \/ /  \  \/ // __ \|  |/ /")
    print("\033[1;34m   \___ \|  |  / /_/ (  <_> )   /|  |\   /\  ___/|    < ")
    print("\033[1;34m  /____  >____/\____ |\____/ \_/ |__| \_/  \___  >__|_ \\")
    print("\033[1;34m       \/           \/                         \/     \/")
    print("\033[0m")
    print("\033[0m")

# Function to find an available port from the given list
def get_available_port(ports):
    for port in ports:
        try:
            server_address = ('', port)
            httpd = socket_server.TCPServer(server_address, HTTPRequestHandler)
            return httpd, port
        except socket.error:
            pass
    return None, None

# Main function
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--http', action='store_true', help='Use HTTP version')
    parser.add_argument('--https', action='store_true', help='Use HTTPS version')
    parser.add_argument('-p', '--port', type=int, help='Specify the port')
    parser.add_argument('-i', '--host', help='Specify the host')
    args = parser.parse_args()

    # Print the banner
    print_banner()

    # Check for valid arguments
    if args.http and args.https:
        print("\033[1;31mError: Only one of --http or --https can be used at a time.\033[0m")
        sys.exit(1)

    if not args.http and not args.https:
        print("\033[1;31mError: Please specify either --http or --https switch.\033[0m")
        sys.exit(1)

    # Set default values
    default_port = 80 if args.http else 443
    default_host = ''

    # Set default values
    default_ports_http = [80, 8000, 8080]
    default_ports_https = [443, 8443, 8444]
    default_host = ''

    # Overwrite default values with provided arguments, if any
    port = args.port if args.port else (default_ports_http if args.http else default_ports_https)
    host = args.host if args.host else default_host

    if not isinstance(port, list):
        port = [port]

    if args.http:
        # HTTP version
        server_address = (host, port[0])
        server, port = get_available_port(port)
        if server is None:
            sys.exit("\033[1;31mError: Could not find an available port for HTTP.\033[0m")
        colored_message = "\033[1;34mServing HTTP on - \033[1;32m{}:{}\033[0m".format(server_address[0] or 'localhost', port)

    else:  # HTTPS version
        server_address = (host, port[0])
        httpd = SecureHTTPServer(server_address, HTTPRequestHandler)
        sa = httpd.socket.getsockname()
        bind_address = sa[0]
        port = sa[1]
        colored_message = "\033[1;34mServing HTTPS on - \033[1;32m{}:{}\033[0m".format(server_address[0] or 'localhost', port)


    # Print server info
    print(colored_message)
    print("\033[0m")

    try:
        if args.http:
            # Start serving HTTP
            server.serve_forever()
        else:
            # Start serving HTTPS
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\033[1;34mBye Bye.. \033[1;32m:)\033[0m")
        if args.http:
            # Close HTTP server
            server.server_close()
        else:
            # Close HTTPS server
            httpd.server_close()
        sys.exit(0)

if __name__ == '__main__':
    main()
