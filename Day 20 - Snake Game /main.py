from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Display keyboard controls
controls = Turtle()
controls.penup()
controls.hideturtle()
controls.color('white')
controls.goto(0, -280)
controls.write("UP = W, DOWN = S, LEFT = A, RIGHT = D", align='center', font=('Courier', 14, 'bold'))


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
        scoreboard.add_score()

    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()













screen.exitonclick()
