from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def draw_square():
    for i in range(3):
        turtle.forward(100)
        turtle.right(90)
    turtle.forward(100)


draw_square()
screen.exitonclick()
