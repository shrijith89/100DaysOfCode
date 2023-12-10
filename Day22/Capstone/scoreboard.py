from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write("Level: {}".format(self.level), align="left", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write("Level: {}".format(self.level), align="left", font=FONT)
