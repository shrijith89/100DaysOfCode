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
        self.highscore = self.read_highscore()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-20, 250)
        self.pendown()
        self.write(f"Score : {self.score} HighScore : {self.highscore}", align=ALIGNMENT, font=FONT)

    def read_highscore(self):
        with open('data.txt') as file:
            content = file.read()
        return int(content)

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
            with open('data.txt', 'w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()
