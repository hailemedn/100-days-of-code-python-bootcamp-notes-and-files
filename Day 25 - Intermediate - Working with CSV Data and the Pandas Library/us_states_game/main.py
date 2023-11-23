from turtle import Turtle, Screen
import pandas

us_map = Turtle()
screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
us_map.shape(image)


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

correct_answers = []
remaining_states = data
while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct",
                                    prompt="what's another state name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in correct_answers:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states and answer_state not in correct_answers:
        state_names = Turtle()
        state_names.hideturtle()
        state_names.penup()
        correct_answers.append(answer_state)
        # gets the row of the correctly answered state
        answer_state_data = data[data.state == answer_state]
        state_names.goto(int(answer_state_data.x), int(answer_state_data.y))
        state_names.write(answer_state)
        # remaining_states = remaining_states[remaining_states.state != answer_state]

# states to learn.csv
# remaining_states.to_csv("states_to_learn.csv")

