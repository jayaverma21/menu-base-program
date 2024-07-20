#!/usr/bin/env python3

import random
import string
import cgi
import cgitb

cgitb.enable()

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types")

    # Character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensuring the password has at least one of each character type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Filling the rest of the password length with a mix of all character types
    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length - 4)

    # Shuffling the result to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    form = cgi.FieldStorage()
    length = form.getvalue("length")

    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head><title>Password Generator</title></head>")
    print("<body>")

    if length:
        try:
            length = int(length)
            password = generate_password(length)
            print(f"<p>Generated password: <strong>{password}</strong></p>")
        except ValueError as ve:
            print(f"<p>Error: {ve}</p>")
        except Exception as e:
            print(f"<p>An unexpected error occurred: {e}</p>")
    else:
        print("<p>Please provide a length for the password.</p>")

    print('<a href="/password_form.html">Go back</a>')

    print("</body>")
    print("</html>")

if __name__ == "__main__":
    main()
