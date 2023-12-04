import time
from turtle import Turtle
import turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape('circle')
        self.penup()

    def move(self):
        new_x = self.xcor() + 5
        new_y = self.ycor() + 5
        time.sleep(0.05)
        self.goto(new_x, new_y)
