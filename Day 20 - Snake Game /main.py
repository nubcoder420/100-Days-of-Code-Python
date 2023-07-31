from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detecting collision of snake head with food
    if snake.head.distance(food) < 15:
        food.refresh()















screen.exitonclick()
