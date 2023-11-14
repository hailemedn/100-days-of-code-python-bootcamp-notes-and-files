from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=500)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -90, -30, 30, 90, 150]
all_turtles = []
for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.shapesize(2, 2, 1)
    new_turtle.color(colors[index])
    new_turtle.goto(-220, y_positions[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
