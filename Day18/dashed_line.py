import time
import turtle as t

turtle = t.Turtle()

for i in range(30):
    t.forward(5)
    t.penup()
    t.forward(5)
    t.pendown()

t.exitonclick()
