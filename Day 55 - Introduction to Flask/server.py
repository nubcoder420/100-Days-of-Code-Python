from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def guess_a_number():
    return f"<h1>Guess a number between 0 and 9</h1>" \
           f"<p>Enter your guess number after the '/' at the URL and press Enter</p>" \
           f"<img src='https://media.giphy.com/media/bbshzgyFQDqPHXBo4c/giphy.gif'>" \


random_number = random.randint(0, 9)

@app.route('/<int:user_guess>')
def display_page(user_guess):
    if user_guess < random_number:
        return f'<h1><span style="color: red;">Too low, try again!</span></h1>' \
               f'<img src="https://media.giphy.com/media/gorK7bQrLJpRu/giphy.gif">'
    elif user_guess > random_number:
        return f'<h1><span style="color: purple;">Too high, try again!</span></h1>' \
               f'<img src="https://media.giphy.com/media/3o7abAHdYvZdBNnGZq/giphy.gif">'
    else:
        return f'<h1><span style="color: green;">Correct!</span></h1>' \
               f'<img src="https://media.giphy.com/media/oDK8A6xUNjD2M/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
