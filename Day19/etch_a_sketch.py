import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def clockwise():
    tim.forward(5)
    tim.right(5)


def counter_clockwise():
    tim.backward(5)
    tim.left(5)


def clr_screen():
    turtle.clearscreen()


screen.listen()
screen.onkey(clockwise, 'd')
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(counter_clockwise, 'a')
screen.onkey(clr_screen, 'c')
screen.exitonclick()
