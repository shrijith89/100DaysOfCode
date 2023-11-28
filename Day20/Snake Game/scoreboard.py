import turtle
from turtle import Turtle, Screen
from turtle import Pen

screen = Screen()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-20, 250)
        self.pendown()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 16, "normal"))
