import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
is_on = True

paddle = Turtle()
paddle.shape('square')
paddle.color('black')
paddle.shapesize(stretch_wid=9, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)
screen.tracer()


def move_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def move_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

screen.listen()



screen.exitonclick()
