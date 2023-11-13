from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)
tim = Turtle()
# tim.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# code challenge - draw a square
# for i in range(4):
#     print(i)
#     tim.forward(100)
#     tim.right(90)

# code challenge - draw a dashed line
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
#     alternative way
#     tim.forward(10)
#     tim.pencolor("white")
#     tim.forward(10)
#     tim.pencolor("black")

# code challenge - draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon


# def change_color():
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     tim.pencolor(r, g, b)
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for no_of_sides in range(3, 11):
#     change_color()
#     draw_shape(no_of_sides)


# code challenge Draw a random walk
# line gets thicker
# colors change
# gets faster

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor(r, g, b)


# directions = [0, 90, 180, 270]
# tim.pensize(20)
# speed_amount = 1
# for _ in range(100):
#     change_color()
#     tim.setheading(random.choice(directions))
#     tim.speed(speed_amount)
#     if speed_amount < 11:
#         speed_amount += 1
#     tim.forward(40)

# code challenge - Draw a spirograph
import math

tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        change_color()
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(1)
screen = Screen()
screen.exitonclick()

# Tuples
# similar to a list.
# a list of items inside a parenthesis
# set in stone, you can't change the values like a list
# my_tuple = (4, 5, 6)
# print(my_tuple[0])  # returns 4
# why use it, when u want to create a list that isn't mutable.



