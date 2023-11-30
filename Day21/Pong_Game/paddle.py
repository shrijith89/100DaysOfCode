from turtle import Turtle

MOVE_SEGMENT = 40
positions = [(350, 20), (350, 40), (350, 60), (350, 80)]

turtle = Turtle()


class Paddle:
    def __init__(self):
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        new_turtle.color('black')
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def move_up(self):
        self.segments[3].setheading(90)
        self.segments[3].forward(MOVE_SEGMENT)
        for turtle1 in range(len(self.segments) - 2, -1, -1):
            new_xcor = self.segments[turtle1].xcor()
            new_ycor = self.segments[turtle1].ycor() + MOVE_SEGMENT
            self.segments[turtle1].goto(new_xcor, new_ycor)

    def move_down(self):
        self.segments[0].setheading(270)
        self.segments[0].forward(MOVE_SEGMENT)
        for turtle1 in range(len(self.segments)-1, 0, -1):
            new_xcor = self.segments[turtle1].xcor()
            new_ycor = self.segments[turtle1].ycor() - MOVE_SEGMENT
            self.segments[turtle1].goto(new_xcor, new_ycor)


