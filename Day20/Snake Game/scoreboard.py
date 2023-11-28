import turtle
from turtle import Turtle
from turtle import Pen

pen = turtle.Turtle()


class Scoreboard:

    def __init__(self):
        turtle.hideturtle()
        pen.penup()
        pen.goto(0, 150)
        pen.pendown()
        turtle.color('white')


        text = turtle.textinput("Input", "Enter text to write:")

        turtle.write(text, align="center", font=("Arial", 16, "normal"))
