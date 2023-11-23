from turtle import Turtle, Screen
import pandas

us_map = Turtle()
screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
us_map.shape(image)

state_names = Turtle()
state_names.hideturtle()
state_names.penup()

data = pandas.read_csv("50_states.csv")
states = data.state
states_list = states.to_list()

x_coordinates = data.x.to_list()
y_coordinates = data.y.to_list()

correct_guesses = 0
correct_answers = []

while correct_guesses != 50:
    guess = screen.textinput(title=f"{correct_guesses}/50 States Correct", prompt="what's another state name?").title()
    if guess in states_list and guess not in correct_answers:
        correct_guesses += 1
        correct_answers.append(guess)

        x_position = x_coordinates[states_list.index(guess)]
        y_position = y_coordinates[states_list.index(guess)]
        state_names.goto(x_position, y_position)
        state_names.write(guess)


screen.exitonclick()
