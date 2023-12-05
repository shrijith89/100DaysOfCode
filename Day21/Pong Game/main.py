from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
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
    screen.update()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 80 and ball.xcor() > 340:
        ball.bounce_x()
    if ball.distance(l_paddle) < 80 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()
