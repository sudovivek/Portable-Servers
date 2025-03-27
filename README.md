# Portable Servers

This repository contains two portable server scripts: one for FTP and another for HTTP/HTTPS.

## FTP Server

The `FTP_server` directory contains a Python script (`ftp-server.py`) for setting up a simple FTP server. It utilizes the `pyftpdlib` library to create the server. 

### Features

- Supports both standard FTP and secure FTPS.
- Customizable configuration options for port, home directory, and user credentials.
- Graceful exit handling.


python ftp-server.py [options]


## HTTP/HTTPS File Server

The `HTTP_server` directory contains a Python script (`http-server.py`) for setting up a simple HTTP/HTTPS file server. It supports file uploads using the PUT, POST & DELETE method and can serve files over HTTP and HTTPS protocols.

### Features

- Supports both HTTP and HTTPS protocols.
- Supports both Python 2 and Python 3.
- Allows file uploads using the PUT & POST method and has a delete method for deleting files.
- Automatically selects an available port from a predefined list.


python http-server.py [options]


### Author

- Author: Vivek Choudhary
- GitHub: [@sudovivek](https://github.com/sudovivek)

### Issues and Feedback

If you encounter any issues or have suggestions for improvement, please open an issue on GitHub.
