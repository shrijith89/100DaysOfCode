import time
import turtle
from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('white')
screen.setup(width=800, height=600)
screen.title("Pong Game")
paddle = Paddle()
is_on = True
screen.tracer(0)
screen.listen()

turtle.onkey(paddle.move_up, "Up")
turtle.onkey(paddle.move_down, "Down")

while is_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
