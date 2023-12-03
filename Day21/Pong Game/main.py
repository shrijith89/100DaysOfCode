from turtle import Turtle, Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)

paddle = Paddle()

# Use the instance 'paddle' to access the methods
screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")

screen.tracer(0)
screen.listen()

game_is_on = True

while game_is_on:
    screen.update()
    
screen.exitonclick()
