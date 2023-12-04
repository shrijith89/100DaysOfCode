from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


screen.tracer(0)
screen.listen()

game_is_on = True

while game_is_on:
    ball.move()
    ball.x_collision()
    ball.y_collision()
    screen.update()


screen.exitonclick()
