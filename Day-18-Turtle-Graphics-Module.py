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

challenge_1()

screen = Screen()
screen.exitonclick()
