# Portable Servers

This repository contains two portable server scripts: one for FTP and another for HTTP/HTTPS.

markdown

## FTP Server

The `ftp_server` directory contains a Python script (`ftp-server.py`) for setting up a simple FTP server. It utilizes the `pyftpdlib` library to create the server. 

### Features

- Supports both standard FTP and secure FTPS.
- Customizable configuration options for port, home directory, and user credentials.
- Graceful exit handling.

### Usage

1. Ensure you have Python installed on your system.
2. Install the required dependencies listed in `requirements.txt`.
3. Run the script with the following command:
   

python ftp-server.py [options]

markdown


Available options:

- `-p` or `--port`: Specify the port number for the FTP server (default is 21).
- `-s` or `--ssl`: Run the server as a secure FTPS server.
- `-l` or `--location`: Set the home directory for FTP users (default is the current directory).
- `-U` or `--user`: Specify the username for FTP login (default is 'benelog').
- `-P` or `--password`: Set the password for FTP login (optional).
- `-i` or `--ip`: Specify the IP address to bind the FTP server to (default is '0.0.0.0').

### License

This script is released under the MIT License. See the [LICENSE](./ftp_server/LICENSE) file for details.

### Author

- Author: SUDOVIVEK
- GitHub: [@sudovivek](https://github.com/sudovivek)

### Contributing

Contributions are welcome. Please open an issue or create a pull request.

### Issues and Feedback

If you encounter any issues or have suggestions for improvement, please open an issue on GitHub.

## HTTP/HTTPS File Server

The `python_server` directory contains a Python script (`python_server.py`) for setting up a simple HTTP/HTTPS file server. It supports file uploads using the PUT method and can serve files over HTTP and HTTPS protocols.

### Features

- Supports both HTTP and HTTPS protocols.
- Supports both Python 2 and Python 3.
- Allows file uploads using the PUT method and has a delete method for deleting files.
- Automatically selects an available port from a predefined list.

### Usage

1. Ensure you have Python 2 or Python 3 installed on your system.
2. Ensure you have the required certificate and key files (`cert.pem` and `key.pem`) in the same directory as the script.
3. Run the script with the following command:

python python_server.py [options]

markdown


Available options:

- `--http`: Use HTTP version (default is HTTPS).
- `--https`: Use HTTPS version (default).
- `-p` or `--port`: Specify the port (default is 80 for HTTP and 443 for HTTPS).
- `-i` or `--host`: Specify the host (default is empty, allowing all interfaces).

### License

This script is released under the MIT License. See the [LICENSE](./python_server/LICENSE) file for details.

### Author

- Author: SUDOVIVEK
- GitHub: [@sudovivek](https://github.com/sudovivek)

### Contributing

Contributions are welcome. Please open an issue or create a pull request.

### Issues and Feedback

If you encounter any issues or have suggestions for improvement, please open an issue on GitHub.

vbnet


Make sure to replace `[options]` in the usage sections with the actual command-line options your scripts support. You can also add more details about the script's functionality, how to obtain the required certificate and key files, and any other relevant information. Additionally, update the "Author" and "GitHub" sections with your information.

2 / 2
Was this response better or worse?
