import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

turtle.onkey(player.move_forward, key='Up')
screen.listen()


game_is_on = True
while game_is_on:
    car_manager.move_car()
    time.sleep(0.1)
    screen.update()
