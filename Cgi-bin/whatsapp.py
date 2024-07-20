#!/usr/bin/python3

import cgi
import cgitb
from twilio.rest import Client

cgitb.enable()  # Enable CGI traceback for debugging

# Print necessary headers
print("Content-Type: text/html\n")

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
phone_number = form.getvalue('phone_number')
message = form.getvalue('message')

def send_whatsapp_message(phone_number, message):
    # Twilio credentials (replace with your actual credentials)
    account_sid = 'Enter your sid'
    auth_token = 'Enter yout auth_token'
    twilio_whatsapp_number = 'whatsapp:enter twilio whatsapp number'  # Twilio's sandbox number

    client = Client(account_sid, auth_token)
    try:
        # Sending the message
        client.messages.create(
            body=message,
            from_=twilio_whatsapp_number,
            to=f'whatsapp:{phone_number}'
        )
        return "Message sent successfully."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if phone_number and message:
    result = send_whatsapp_message(phone_number, message)
else:
    result = "All form fields are required."

print(f"<html><body><h1>{result}</h1></body></html>")
