#!/usr/bin/env python3

import cgi
import cgitb
import pyqrcode

cgitb.enable()

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
url = form.getvalue('url')

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>QR Code Generator</title>
</head>
<body>
    <h1>QR Code Generator</h1>
    <form method="post" action="/cgi-bin/qr_generator.py">
        <label for="url">Enter URL:</label>
        <input type="text" id="url" name="url" required>
        <input type="submit" value="Generate QR Code">
    </form>
    <div class="result">
        {}
    </div>
</body>
</html>
"""

if url:
    try:
        qr_code = pyqrcode.create(url)
        qr_code_file = "/var/www/html/myqr.svg"  # Adjust the path based on your web server's document root
        qr_code.svg(qr_code_file, scale=8)
        img_tag = f'<img src="/myqr.svg" alt="QR Code">'
        print(html_template.format(img_tag))
    except Exception as e:
        print(html_template.format(f"Error generating QR code: {e}"))
else:
    print(html_template.format("Please enter a URL"))
