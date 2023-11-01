import os
import argparse
import signal
from ftplib import FTP
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


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

# Print the banner
print_banner()


def setup_ftp_server(config):
    authorizer = DummyAuthorizer()
    user = config['user']
    password = config['password']
    home_directory = config['location']
    
    if password:
        authorizer.add_user(user, password, home_directory, perm='elradfmw')
    else:
        authorizer.add_anonymous(home_directory)

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer((config['ip'], config['port']), handler)
    return server

def graceful_exit(signum, frame):
    exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, graceful_exit)
    
    parser = argparse.ArgumentParser(description="Run a simple FTP server")
    parser.add_argument('-p', '--port', type=int, default=21, help='Port number for the FTP server')
    parser.add_argument('-s', '--ssl', action='store_true', help='Run FTP secure version (FTPS)')
    parser.add_argument('-l', '--location', type=str, default=os.getcwd(), help='Home directory for FTP users')
    parser.add_argument('-U', '--user', type=str, default='benelog', help='Username for FTP login')
    parser.add_argument('-P', '--password', type=str, help='Password for FTP login')
    parser.add_argument('-i', '--ip', type=str, default='0.0.0.0', help='IP address to bind the FTP server to')
    
    args = parser.parse_args()
    
    config = {
        'ip': args.ip,
        'port': args.port,
        'passive_ports': range(10125, 10200),  # Range of passive ports
        'ssl': args.ssl,
        'user': args.user,
        'password': args.password,
        'location': args.location
    }

    server = setup_ftp_server(config)
    if args.ssl:
        print("\033[1;34mStarting Secure FTPS Server On - \033[1;32m{}:{}\033[0m\n".format(config['ip'] or 'localhost', config['port']))
        server.tls_control_required = True
    else:
        print("\033[1;34mStarting FTP Server On - \033[1;32m{}:{}\033[0m\n".format(config['ip'] or 'localhost', config['port']))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    print("\n\033[1;34mBye Bye.. \033[1;32m:)\033[0m")

