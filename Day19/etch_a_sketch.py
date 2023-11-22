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
screen.onkey(clockwise, 'D')
screen.onkey(move_forwards, 'W')
screen.onkey(move_backwards, 'S')
screen.onkey(counter_clockwise, 'A')
screen.onkey(clr_screen, 'C')
screen.exitonclick()
