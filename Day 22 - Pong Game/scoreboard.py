from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.l_score, align='center', font=('Courier', 30, 'bold'))
        self.goto(100, 230)
        self.write(self.r_score, align='center', font=('Courier', 30, 'bold'))

    def add_score_left(self):
        self.l_score += 1
        self.update_scoreboard()

    def add_score_right(self):
        self.r_score += 1
        self.update_scoreboard()