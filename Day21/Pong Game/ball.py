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

    def detect_collision(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.dx *= -1
        elif self.xcor() > 290 or self.xcor() < -290:
            self.dx *= -1
