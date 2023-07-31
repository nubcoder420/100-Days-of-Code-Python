from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game by nubcoder420')
screen.tracer(0)

scoreboard = Scoreboard()

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")
screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    # Detect collision with the right wall
    if ball.xcor() > 380:
        scoreboard.add_score_left()
        ball.reset_position()

    # Detect collision with the left wall
    if ball.xcor() < -380:
        scoreboard.add_score_right()
        ball.reset_position()


screen.exitonclick()
