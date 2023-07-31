from turtle import Turtle

MOVEMENT_SPEED = 30

class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()

        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, y_pos)

    def go_up(self):
        new_y_pos = self.ycor() + MOVEMENT_SPEED
        self.goto(self.xcor(), new_y_pos)

    def go_down(self):
        new_y_pos = self.ycor() - MOVEMENT_SPEED
        self.goto(self.xcor(), new_y_pos)