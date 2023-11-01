# Python FTP Server

This Python script creates a simple FTP server with the option to run it as a secure FTP server (FTPS). It allows you to easily set up an FTP server with various configuration options.

## Features

- Supports both standard FTP and secure FTPS.
- Customizable configuration options for port, home directory, and user credentials.
- Passive mode support with a range of passive ports.
- Graceful exit handling.

## Usage

1. Ensure you have Python installed on your system.

2. Download the script, and make sure you have the required dependencies installed.

3. Run the script with the following command:

   ```bash
   python ftp_server.py [options]

Available options:

    -p or --port: Specify the port number for the FTP server (default is 21).
    -s or --ssl: Run the server as a secure FTPS server.
    -l or --location: Set the home directory for FTP users (default is the current directory).
    -U or --user: Specify the username for FTP login (default is 'benelog').
    -P or --password: Set the password for FTP login (optional).
    -i or --ip: Specify the IP address to bind the FTP server to (default is '0.0.0.0').

    The script will start serving files, and you can access the FTP server using an FTP client.

Configuration

You can customize the FTP server configuration by modifying the command-line options when running the script.
SSL/TLS

If you use the -s or --ssl option, the server will run in secure FTPS mode, and you should connect using an FTPS client. The script provides secure FTP functionality by default.
License

This script is released under the MIT License. See the LICENSE file for details.
Author

    Author: SUDOVIVEK
    GitHub: @sudovivek

Contributing

Contributions are welcome. Please open an issue or create a pull request.
Issues and Feedback

If you encounter any issues or have suggestions for improvement, please open an issue on GitHub.
Acknowledgments

Special thanks to the community and contributors for their support and feedback.


Please replace `[options]` in the usage section with the actual command-line options your script supports. You can also add more details about the script's functionality, how to obtain the required dependencies, and any other relevant information. Additionally, update the "Author" and "GitHub" sections with your information.
