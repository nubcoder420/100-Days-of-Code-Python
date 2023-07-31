from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.color('white')
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align='center', font=('Arial', 12, 'bold'))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
