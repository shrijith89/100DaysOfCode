import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
#user_bet = screen.textinput(title="Choose Color", prompt="Which turtle is going to win the race, Choose your color")
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']

ycor = -200
xcor = -260

for i in range(6):
    t = Turtle(shape='turtle')
    t.penup()
    t.color(colors[i])
    t.goto(xcor, ycor)
    ycor += 40

screen.exitonclick()
