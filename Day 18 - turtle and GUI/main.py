import random
import turtle
from turtle import Turtle, Screen
# import colorgram
#
# colors = colorgram.extract('hirst_painting.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(210, 163, 107), (235, 220, 227), (20, 28, 57), (142, 60, 93),
              (227, 208, 127), (208, 129, 144), (213, 77, 103), (83, 116, 97), (59, 92, 140), (127, 152, 141),
              (68, 21, 41),
              (127, 33, 55), (40, 52, 105), (143, 72, 55), (226, 181, 164), (230, 162, 178), (138, 155, 177),
              (92, 126, 173),
              (113, 135, 122), (178, 110, 94), (183, 188, 205), (185, 199, 180), (37, 85, 62), (208, 122, 41),
              (34, 71, 53),
              (44, 70, 78), (111, 47, 35)]

# my solution
# turtle.colormode(255)
# tim = Turtle()
# tim.penup()
#
# yposition = -200
#
#
# def draw_a_line():
#     for _ in range(10):
#         tim.dot(20, random.choice(color_list))
#         tim.forward(50)
#
#
#
#
# for _ in range(10):
#     draw_a_line()
#     yposition += 50
#     tim.sety(yposition)
#     tim.setx(0)

# Angela's solution
# turtle.colormode(255)
# tim = Turtle()
# tim.penup()
# tim.speed("fastest")
# tim.hideturtle()
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# num_of_dots = 100
# for dots in range(1, num_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dots % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)


screen = Screen()
screen.exitonclick()
