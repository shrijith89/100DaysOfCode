import turtle
from turtle import Turtle

MOVE_SEGMENT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for turtle1 in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[turtle1 - 1].xcor()
            new_ycor = self.segments[turtle1 - 1].ycor()
            self.segments[turtle1].goto(new_xcor, new_ycor)
        self.segments[0].forward(MOVE_SEGMENT)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)
