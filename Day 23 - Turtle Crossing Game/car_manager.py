from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.2


class CarManager:

    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape('square')
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.rand_x = random.randint(300, 500)
        new_car.rand_y = random.randrange(-220, 240, 20)
        new_car.goto(new_car.rand_x, new_car.rand_y)
        self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def increase_speed(self):
        for car in self.car_list:
            self.car_speed += MOVE_INCREMENT
