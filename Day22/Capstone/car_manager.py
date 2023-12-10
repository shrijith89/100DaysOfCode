from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = [(290, 0), (260, 20), (210, 0)]


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        choice = random.randrange(0, 6)
        if choice == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y = random.randrange(-250, 250)
            new_car.goto(280, y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)