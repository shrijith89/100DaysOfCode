import random
import time
import turtle as t
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
color = ['red', 'green', 'blue']
is_on = True
screen.tracer(0)


all_turtles = []
xcor = 0
dist = 0

for i in range(3):
    new_turtle = Turtle(shape='square')
    new_turtle.color('white')
    new_turtle.penup()
    new_turtle.forward(dist)
    all_turtles.append(new_turtle)
    dist += 20

while is_on:
    for turtle1 in all_turtles:
        turtle1.forward(60)
        screen.update()
        time.sleep(0.1)

screen.exitonclick()
