from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('black')
        self.shapesize(stretch_wid=9, stretch_len=1)
        self.penup()
        self.goto(350, 0)


    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
