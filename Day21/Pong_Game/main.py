import time
import turtle
from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('white')
screen.setup(width=800, height=600)
screen.title("Pong Game")
paddle = Paddle()


screen.exitonclick()
