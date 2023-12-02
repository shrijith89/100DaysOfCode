import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)

paddle = Turtle()
paddle.shape('square')
paddle.color('black')
paddle.shapesize(stretch_wid=9, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)
screen.tracer()
screen.exitonclick()
