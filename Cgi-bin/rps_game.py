#!/usr/bin/env python3

import cgi
import cgitb
import random

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
player_choice = form.getvalue("choice")

t = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(t)

result = ""
if player_choice:
    if player_choice == computer_choice:
        result = "Tie!"
    elif player_choice == "Rock":
        if computer_choice == "Paper":
            result = "You lose! Paper covers Rock."
        else:
            result = "You win! Rock smashes Scissors."
    elif player_choice == "Paper":
        if computer_choice == "Scissors":
            result = "You lose! Scissors cut Paper."
        else:
            result = "You win! Paper covers Rock."
    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            result = "You lose! Rock smashes Scissors."
        else:
            result = "You win! Scissors cut Paper."
    else:
        result = "That's not a valid play. Check your spelling!"
else:
    result = "Please make a choice."
    
print(result)
