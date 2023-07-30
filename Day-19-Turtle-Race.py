from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
dudes = []

user_bet = screen.textinput(title="Turtle Race: Place your bet!", prompt=f"Choose a color {colors}").lower()

y_pos = -100

for turtle_index in range(0, 6):

    new_dude = Turtle(shape='turtle')
    new_dude.penup()

    new_dude.color(colors[turtle_index])
    new_dude.goto(x=-220, y=y_pos)

    y_pos += 40

    dudes.append(new_dude)

if user_bet:
    is_race_on = True

while is_race_on:

    for dude in dudes:
        if dude.xcor() > 230:
            is_race_on = False
            winner = dude.pencolor()
            if winner == user_bet:
                screen.title(f"You win! The {winner} dude finished first!")
            else:
                screen.title(f"You lost! The {winner} dude finished first!")

        random_steps = random.randint(0, 10)
        dude.forward(random_steps)


screen.exitonclick()
