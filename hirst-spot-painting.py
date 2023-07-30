import turtle as t
from turtle import Screen
import random

color_list = [
        (238, 236, 234), (230, 226, 228), (34, 108, 167), (223, 229, 235), (227, 233, 230), (245, 77, 36),
        (112, 163, 211), (153, 57, 85), (219, 156, 94), (201, 60, 27), (24, 133, 55), (246, 204, 84),
        (190, 151, 47), (225, 119, 152), (46, 53, 121), (221, 68, 97), (113, 199, 156), (147, 37, 30),
        (253, 202, 0), (91, 113, 192), (74, 40, 32), (248, 153, 143), (111, 41, 49), (155, 212, 203),
        (53, 174, 163), (38, 31, 67), (154, 210, 219), (43, 33, 45), (35, 55, 46), (99, 93, 2),
        (43, 151, 190), (10, 111, 51), (228, 169, 182), (177, 186, 217)
]

t.colormode(255)

spot = t.Turtle()

spot.speed(0)
spot.penup()
spot.hideturtle()


x = -298
y = -298

def create_row():
    global x, y
    for _ in range(16):

        spot.color(random.choice(color_list))
        spot.setpos(x, y)
        spot.dot(20)
        x += 40

    y += 40
    x = -298
    spot.setposition(x, y)

for _ in range(16):
    create_row()


my_screen = Screen()
my_screen.screensize(400, 300)
my_screen.exitonclick()
