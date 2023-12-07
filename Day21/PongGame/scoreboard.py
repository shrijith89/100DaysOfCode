from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-50, 250)
        self.write(self.lscore, align=ALIGNMENT, font=FONT)
        self.goto(50, 250)
        self.write(self.rscore, align=ALIGNMENT, font=FONT)

    def l_score(self):
        self.lscore += 1
        self.clear()
        self.update_scoreboard()

    def r_score(self):
        self.rscore += 1
        self.clear()
        self.update_scoreboard()
