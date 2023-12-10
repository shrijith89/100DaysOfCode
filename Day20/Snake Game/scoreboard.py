import turtle
from turtle import Turtle, Screen
from turtle import Pen

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

screen = Screen()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-20, 250)
        self.pendown()
        self.write(f"Score : {self.score} HighScore : {self.highscore}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} HighScore : {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score} Highscore : {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
