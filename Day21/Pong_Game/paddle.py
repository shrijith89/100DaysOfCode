from turtle import Turtle

positions = [(0, 20),(0, 40), (0, 60)]

turtle = Turtle()


class Paddle:
    def __init__(self):
        new_turtle = Turtle(shape='square')
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)
