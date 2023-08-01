from turtle import Turtle

FONT = ("Courier", 14, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.level = 1

    def update_level(self):
        self.clear()
        self.goto(-240, 260)
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def add_level(self):
        self.level += 1

    def game_over(self):
        self. goto(0, 0)
        self.write(f"GAME OVER !", align='center', font=FONT)
