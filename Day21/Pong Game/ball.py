import time
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape('circle')
        self.dx = 2
        self.dy = -2
        self.penup()

    def move(self):
        new_x = self.xcor() + 5
        new_y = self.ycor() + 5
        time.sleep(0.05)
        self.goto(new_x, new_y)

    def y_collision(self):
        if self.ycor() > 270 or self.ycor() < -270:
            self.dx *= -1

    def x_collision(self):
        if self.xcor() > 270 or self.xcor() < -270:
            self.dx *= -1
