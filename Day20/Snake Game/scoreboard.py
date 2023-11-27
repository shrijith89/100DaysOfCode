import turtle
from turtle import Turtle


class Scoreboard:
    def __init__(self):
        turtle.hideturtle()
        turtle.color('white')
        turtle.write((280, 280), "Home= ", False, align="center")
        #turtle.write((280, 280), True)
