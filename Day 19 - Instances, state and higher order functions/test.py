from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def move_left():
#     tim.left(10)
#     tim.forward(10)
#
#
# def move_right():
#     tim.right(10)
#     tim.forward(10)
#
#
# def clear_screen():
#     screen.reset()
#
#
# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()

# code challenge - make an Etch A sketch app

# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="c", fun=clear_screen)

tim2 = Turtle()
tim2.sety(100)
tim2.shape("turtle")
tim2.color("blue")

tim.shape("turtle")
screen.exitonclick()
