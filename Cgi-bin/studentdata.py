#!/usr/bin/env python3

import cgi
import cgitb

cgitb.enable()

def print_student_info(form, index):
    name = form.getvalue(f'name_{index}')
    dob = form.getvalue(f'dob_{index}')
    instagram_id = form.getvalue(f'instagram_id_{index}')
    email = form.getvalue(f'email_{index}')
    contact = form.getvalue(f'contact_{index}')
    
    print(f"<h3>Student {index + 1}</h3>")
    if data_selection == 'name':
        print(f"<p>Name: {name}</p>")
    elif data_selection == 'dob':
        print(f"<p>DOB: {dob}</p>")
    elif data_selection == 'instagram_id':
        print(f"<p>Instagram ID: {instagram_id}</p>")
    elif data_selection == 'email':
        print(f"<p>Email: {email}</p>")
    elif data_selection == 'contact':
        print(f"<p>Contact: {contact}</p>")

form = cgi.FieldStorage()
print("Content-type: text/html")
print()
print("<html><body>")
print("<h1>Submitted Student Information</h1>")

# Determine the number of students based on the fields submitted
index = 0
while form.getvalue(f'name_{index}') is not None:
    index += 1

# Get the selected range and data type
start = int(form.getvalue('start_range'))
end = int(form.getvalue('end_range'))
data_selection = form.getvalue('data_selection_value')

# Print student information within the specified range
for i in range(start - 1, min(end, index)):
    print_student_info(form, i)

print("</body></html>")
