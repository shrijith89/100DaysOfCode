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
car = CarManager()

game_is_on = True
flag = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
