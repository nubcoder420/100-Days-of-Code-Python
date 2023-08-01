import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_level()

    car_manager.move()

    # Frequency of generated cars
    if random.randint(1, 6) == 1:
        car_manager.generate_car()

    if player.ycor() > 280:  # 280 finish line
        scoreboard.add_level()
        player.reset_position()
        car_manager.increase_speed()

    # Detect collision
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
