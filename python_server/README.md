# Python Portable HTTP/HTTPS File Server

This Python script is a simple HTTP/HTTPS file server that allows you to upload and download files using the PUT method. It can serve files over HTTP and HTTPS protocols.

## Usage

To use this script, follow these steps:

1. Ensure you have Python 2 or Python 3 installed on your system.

2. Download the script, and make sure you have the required certificate and key files (cert.pem and key.pem) in the same directory.

3. Run the script with the following command:

   ```bash
   python file_server.py [options]


Available options:

    --http: Use HTTP version (default is HTTPS).
    --https: Use HTTPS version (default).
    -p or --port: Specify the port (default is 80 for HTTP and 443 for HTTPS).
    -i or --host: Specify the host (default is empty, allowing all interfaces).

    The script will start serving files, and you can access the file server via a web browser or other HTTP/HTTPS clients.

Features

    Supports both HTTP and HTTPS protocols.
    Supports both python version "2.7" & "3".
    Allows file uploads using the PUT method also have delete method for deleting files.
    Automatically selects an available port from a predefined list.

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


You should replace `[options]` in the usage section with the actual command-line options your script supports. You can also add more details about the script's functionality, how to obtain the required certificate and key files, and any other relevant information. Additionally, update the "Author" and "GitHub" sections with your information.
