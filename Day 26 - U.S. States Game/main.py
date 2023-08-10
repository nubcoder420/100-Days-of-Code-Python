import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game by nubcoder420")
screen.setup(800, 600)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
data_dict = data.to_dict()

correct_answers = []

while len(correct_answers) < 50:

    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States correct",
                                    prompt="Enter a state's name").title()

    if answer_state == "Exit":
        # missing_states = []
        # for state in state_list:
        #     if state not in correct_answers:
        #         missing_states.append(state)

        # using list comprehension
        missing_states = [state for state in state_list if state not in correct_answers]

        df = pandas.DataFrame(missing_states)
        df.to_csv("States_to_learn.csv")

        break

    if answer_state in state_list:

        correct_answers.append(answer_state)

        state_index = state_list.index(answer_state)
        state_x = data_dict["x"][state_index]
        state_y = data_dict["y"][state_index]

        turtle2 = turtle.Turtle()
        turtle2.penup()
        turtle2.hideturtle()
        turtle2.goto(state_x, state_y)
        turtle2.write(answer_state)


