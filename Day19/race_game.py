import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
user_bet = screen.textinput(title="Choose Color", prompt="Which turtle is going to win the race, Choose your color")
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']
all_turtles = []
race_is_on = False
winner = ""
ycor = -200
xcor = -260

for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(xcor, ycor)
    ycor += 40
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for trtle in all_turtles:
        trtle.forward(random.randint(1, 10))
        if trtle.xcor() >= 260:
            winner = trtle.color()[0]
            race_is_on = False

if winner == user_bet:
    print("Your guess was right")
else:
    print("You lost! {} won the race".format(winner))
