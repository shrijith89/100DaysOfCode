import turtle
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
#user_bet = screen.textinput(title="Choose Color", prompt="Which turtle is going to win the race, Choose your color")

t.hideturtle()
turtle.penup()
turtle.goto(-280, -250)
screen.exitonclick()
