
#!/usr/bin/env python3

import random
import cgi
import cgitb

cgitb.enable()

words = ["python", "hangman", "computer", "programming", "challenge"]

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    form = cgi.FieldStorage()
    letter = form.getvalue("letter")
    state = form.getvalue("state")
    
    if not state:
        word_to_guess = choose_word()
        guessed_letters = []
        attempts = 6
    else:
        state = eval(state)
        word_to_guess = state["word_to_guess"]
        guessed_letters = state["guessed_letters"]
        attempts = state["attempts"]
    
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head><title>Hangman Game</title>")
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
    print(".result, .attempts {")
    print("margin-top: 20px;")
    print("color: #333;")
    print("}")
    print(".back-link {")
    print("display: block;")
    print("margin-top: 20px;")
    print("color: #66a6ff;")
    print("text-decoration: none;")
    print("}")
    print("</style>")
    print("</head>")
    print("<body>")
    print('<div class="container">')
    print("<h1>Hangman Game</h1>")

    if letter:
        if letter in guessed_letters:
            result = "You've already guessed that letter."
        elif letter in word_to_guess:
            guessed_letters.append(letter)
            result = "Good guess!"
            if set(word_to_guess).issubset(set(guessed_letters)):
                result = f"Congratulations! You've guessed the word: {word_to_guess}"
        else:
            guessed_letters.append(letter)
            attempts -= 1
            result = "Wrong guess!"
    else:
        result = ""

    if attempts == 0:
        result = f"You ran out of attempts. The word was: {word_to_guess}"

    state = {"word_to_guess": word_to_guess, "guessed_letters": guessed_letters, "attempts": attempts}
    
    print(f'<div class="result">{result}</div>')
    print(f'<div class="attempts">Word: {display_word(word_to_guess, guessed_letters)}</div>')
    print(f'<div class="attempts">Attempts left: {attempts}</div>')

    print('<form method="post" action="/cgi-bin/hangman_game.py">')
    print('<label for="letter">Guess a letter:</label>')
    print('<input type="text" id="letter" name="letter" maxlength="1" required>')
    print(f'<input type="hidden" name="state" value="{state}">')
    print('<input type="submit" value="Guess">')
    print('</form>')

    print("</div>")
    print("</body>")
    print("</html>")

if __name__ == "__main__":
    main()
