import turtle
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        turtle.setheading(90)
        turtle.penup()
        turtle.goto(STARTING_POSITION)
        turtle.shape('turtle')

