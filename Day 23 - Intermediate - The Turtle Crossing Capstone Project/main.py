import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

STARTING_POSITION = (0, -280)
SLEEPING_TIME = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(SLEEPING_TIME)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    # detect collision with a car
    for car in car_manager.cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.go_to_start()
        car_manager.level_up()
        print(SLEEPING_TIME)


screen.exitonclick()
