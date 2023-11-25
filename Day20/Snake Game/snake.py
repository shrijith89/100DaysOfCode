from turtle import Turtle

MOVE_SEGMENT = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        dist = 20
        for i in range(3):
            new_turtle = Turtle(shape='square')
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.forward(dist)
            self.segments.append(new_turtle)
            dist += 20

    def move(self):
        for turtle1 in range(len(self.segments)-1, 0, -1):
            new_xcor = self.segments[turtle1 - 1].xcor()
            new_ycor = self.segments[turtle1 - 1].ycor()
            self.segments[turtle1].goto(new_xcor, new_ycor)
        self.segments[0].forward(MOVE_SEGMENT)
