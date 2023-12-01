from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        new_turtle = Turtle("circle")
        new_turtle.dot(20, 'white')
