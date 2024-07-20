#!/usr/bin/env python3

import random
import cgi
import cgitb

cgitb.enable()

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    form = cgi.FieldStorage()
    sides = form.getvalue("sides")
    
    if sides:
        sides = int(sides)
        result = roll_dice(sides)
    else:
        result = None
    
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head><title>Dice Rolling Game</title>")
    print("<style>")
    print("body {")
    print("background: linear-gradient(to right, #89f7fe, #66a6ff);")
    print("font-family: Arial, sans-serif;")
    print("display: flex;")
    print("justify-content: center;")
    print("align-items: center;")
    print("height: 100vh;")
    print("margin: 0;")
    print("}")
    print(".container {")
    print("background-color: white;")
    print("padding: 20px;")
    print("border-radius: 10px;")
    print("box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);")
    print("text-align: center;")
    print("}")
    print("h1 {")
    print("color: #333;")
    print("}")
    print(".result {")
    print("margin-top: 20px;")
    print("color: #333;")
    
    print("}")
    print("</style>")
    print("</head>")
    print("<body>")
    print('<div class="container">')
    print("<h1>Dice Rolling Game</h1>")
    
    if result:
        print(f'<div class="result">You rolled a {sides}-sided dice and got: {result}</div>')
    else:
        print('<div class="result">Enter the number of sides and roll the dice!</div>')
    
    print('<form method="post" action="/cgi-bin/dice_roll_game.py">')
    
    print("</div>")
    print("</body>")
    print("</html>")

if __name__ == "__main__":
    main()
