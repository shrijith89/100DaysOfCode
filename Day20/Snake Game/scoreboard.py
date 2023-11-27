import turtle
from turtle import Turtle
from turtle import Pen

pen = turtle.Turtle()


class Scoreboard:
    def __init__(self):
        turtle.hideturtle()
        turtle.color('white')
        pen.up()
        pen.goto(250, 250)
        pen.pendown()
        turtle.write("Home= ", False, align="center")
