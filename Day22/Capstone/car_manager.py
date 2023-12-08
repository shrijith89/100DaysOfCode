from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape('square')
        self.color('red')
        self.shapesize(stretch_wid=1, stretch_len=2)

    def move_car(self):
        self.backward(STARTING_MOVE_DISTANCE)
