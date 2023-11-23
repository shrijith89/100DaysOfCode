import random
import turtle as t
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
color = ['red', 'green', 'blue']

all_turtles = []
xcor = 0
dist = 0

for i in range(3):
    new_turtle = Turtle(shape='square')
    new_turtle.color('white')
    new_turtle.penup()
    new_turtle.forward(dist)
    dist += 20

screen.exitonclick()
