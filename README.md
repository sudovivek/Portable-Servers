# Portable Servers

This repository contains two portable server scripts: one for FTP and another for HTTP/HTTPS.

## FTP Server

The `ftp_server` directory contains a Python script (`ftp-server.py`) for setting up a simple FTP server. It utilizes the `pyftpdlib` library to create the server. 

### Features

- Supports both standard FTP and secure FTPS.
- Customizable configuration options for port, home directory, and user credentials.
- Graceful exit handling.


python ftp-server.py [options]


## HTTP/HTTPS File Server

The `python_server` directory contains a Python script (`http_server.py`) for setting up a simple HTTP/HTTPS file server. It supports file uploads using the PUT, POST & DELETE method and can serve files over HTTP and HTTPS protocols.

### Features

- Supports both HTTP and HTTPS protocols.
- Supports both Python 2 and Python 3.
- Allows file uploads using the PUT method and has a delete method for deleting files.
- Automatically selects an available port from a predefined list.


python http_server.py [options]

markdown

### License

This script is released under the MIT License. See the [LICENSE](./python_server/LICENSE) file for details.

### Author

- Author: SUDOVIVEK
- GitHub: [@sudovivek](https://github.com/sudovivek)

### Issues and Feedback

If you encounter any issues or have suggestions for improvement, please open an issue on GitHub.
