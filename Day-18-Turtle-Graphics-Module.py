from turtle import Turtle, Screen
import random

t = Turtle()
t.shape('turtle')
t.color('DarkRed')

def draw_shape(no_of_sides):

    angle = 360 / no_of_sides

    for _ in range(no_of_sides):
        t.forward(100)
        t.right(angle)

def change_pen_color():
    r = random.random()
    g = random.random()
    b = random.random()

    t.color(r, g, b)


def challenge_1():
    """Challenge 1: Draw a shape according to no of sides and change its color"""
    for shape_sides in range(3, 11):

        draw_shape(shape_sides)
        change_pen_color()
        shape_sides += 1

def left_or_right():

    turn = ['left', 'right']
    random_turn = random.choice(turn)

    if random_turn == 'left':
        t.left(90)
    else:
        t.right(90)

def forward_or_backward(no_of_steps):

    move = ['forward', 'backward']
    random_move = random.choice(move)

    if random_move == 'forward':
        t.forward(no_of_steps)
    else:
        t.back(no_of_steps)


def random_walk1(no_of_moves):

    t.pensize(10)
    t.speed(0)

    for _ in range(no_of_moves):
        forward_or_backward(20)
        left_or_right()
        change_pen_color()

def random_walk2(no_of_moves):

    t.pensize(10)
    t.speed(0)
    direction = [0, 90, 180, 270]

    for _ in range(no_of_moves):
        t.forward(20)
        t.setheading(random.choice(direction))
        change_pen_color()


screen = Screen()
screen.exitonclick()
