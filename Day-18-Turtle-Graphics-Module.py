import turtle as t
from turtle import Screen
import random

pen1 = Turtle()
# t.shape('turtle')
# t.color('DarkRed')
t.colomode(255)

def draw_shape(no_of_sides):

    angle = 360 / no_of_sides

    for _ in range(no_of_sides):
        pen1.forward(100)
        pen1.right(angle)

def change_pen_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color


def challenge_1():
    """Challenge 1: Draw a shape according to no of sides and change its color"""
    for shape_sides in range(3, 11):

        draw_shape(shape_sides)
        pen1.color(change_pen_color())
        shape_sides += 1

def left_or_right():

    turn = ['left', 'right']
    random_turn = random.choice(turn)

    if random_turn == 'left':
        pen1.left(90)
    else:
        pen1.right(90)

def forward_or_backward(no_of_steps):

    move = ['forward', 'backward']
    random_move = random.choice(move)

    if random_move == 'forward':
        pen1.forward(no_of_steps)
    else:
        pen1.back(no_of_steps)


def random_walk1(no_of_moves):

    pen1.pensize(10)
    pen1.speed(0)

    for _ in range(no_of_moves):
        pen1.color(change_pen_color())
        forward_or_backward(20)
        left_or_right()
        

def random_walk2(no_of_moves):

    pen1.pensize(10)
    pen1.speed(0)
    direction = [0, 90, 180, 270]

    for _ in range(no_of_moves):
        pen1.forward(20)
        pen1.setheading(random.choice(direction))
        change_pen_color()

### SPIROGRAPH ###
pen2 = t.Turtle()
pen2.speed(0)

for _ in range(int(360 / 5)):
    pen2.color(change_pen_color())
    pen2.circle(100)
    pen2.setheading(pen2.heading() + 5)


screen = Screen()
screen.exitonclick()
