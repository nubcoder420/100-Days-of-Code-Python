from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 12, 'bold')

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
        self.clear()
        with open('data.txt', mode='r') as all_time_high:
            highest_score = all_time_high.read()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as all_time_high:
                all_time_high.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER !", align=ALIGNMENT, font=FONT)
