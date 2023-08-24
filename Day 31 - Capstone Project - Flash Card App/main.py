from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

#----------------------- DATA SETUP ------------------------#

data = pd.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")

#----------------------- FUNCTIONS ------------------------#

def generate_french_word():
    random_french_word = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=random_french_word['French'])


#----------------------- UI SETUP ------------------------#

window = Tk()
window.title("Flashy by nubcoder420")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400,150, text="title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

x_img = PhotoImage(file="./images/wrong.png")
x_button = Button(image=x_img, highlightthickness=0, command=generate_french_word)
x_button.grid(row=1, column=0)

check_img = PhotoImage(file="./images/right.png")
check_button = Button(image=check_img, highlightthickness=0, command=generate_french_word)
check_button.grid(row=1, column=1)

generate_french_word()

window.mainloop()
