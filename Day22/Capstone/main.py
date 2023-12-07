import time
import turtle
from turtle import Screen
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
turtle.onkey(player.move_forward, key='Up')
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
