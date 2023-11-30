import turtle
from turtle import Turtle, Screen
from paddle import Paddle

MOVE_PADDLE = 40
is_on = True

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong Game")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.tracer(0)

screen.listen()

turtle.onkey(l_paddle.move_up, "w")
turtle.onkey(l_paddle.move_down, "s")


while is_on:
    screen.update()

screen.exitonclick()
