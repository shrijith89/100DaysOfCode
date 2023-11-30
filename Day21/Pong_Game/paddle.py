from turtle import Turtle

MOVE_PADDLE = 40


class Paddle:
    def __init__(self):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color('white')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(350, 0)

    def move_up(self):
        new_y = self.paddle.ycor() + MOVE_PADDLE
        self.paddle.goto(self.paddle.xcor(), new_y)

    def move_down(self):
        new_y = self.paddle.ycor() - MOVE_PADDLE
        self.paddle.goto(self.paddle.xcor(), new_y)
