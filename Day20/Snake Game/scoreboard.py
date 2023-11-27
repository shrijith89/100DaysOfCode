import turtle
from turtle import Turtle
from turtle import Pen

pen = turtle.Turtle()


class Scoreboard:

    def __init__(self):
        turtle.hideturtle()
        pen.up()
        pen.goto(50, 50)
        pen.pendown()
        turtle.color('white')
        turtle.write("Home= ", False, align="center")
