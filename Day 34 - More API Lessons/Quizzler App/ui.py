from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question = self.canvas.create_text(
            150,
            125,
            text="Questions placeholder",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )

        self.score = Label(text="Score: 0", highlightthickness=0, bg=THEME_COLOR, fg="white")
        self.score.config(pady=20,padx=20)
        self.score.grid(row=0, column=1)

        self.true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        self.true_button.config(padx=20, pady=20)

        self.false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0)
        self.false_button.grid(row=2, column=1)
        self.false_button.config(padx=20, pady=20)

        self.window.mainloop()
