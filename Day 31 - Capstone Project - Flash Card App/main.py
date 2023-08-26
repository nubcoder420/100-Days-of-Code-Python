from tkinter import *

import pandas
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
random_french_word = {}
data_dict = {}

#----------------------- DATA SETUP ------------------------#
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

#----------------------- FUNCTIONS ------------------------#

def generate_french_word():
    global random_french_word, flip_timer
    window.after_cancel(flip_timer)
    random_french_word = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_french_word['French'], fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_french_word["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_img)


def is_known():
    data_dict.remove(random_french_word)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_french_word()

#----------------------- UI SETUP ------------------------#

window = Tk()
window.title("Flashy by nubcoder420")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400,150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

x_img = PhotoImage(file="./images/wrong.png")
x_button = Button(image=x_img, highlightthickness=0, command=generate_french_word)
x_button.grid(row=1, column=0)

check_img = PhotoImage(file="./images/right.png")
check_button = Button(image=check_img, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

generate_french_word()



window.mainloop()
