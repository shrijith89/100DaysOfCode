import turtle as t
import random

colors = ['red', 'blue', 'purple', 'red', 'green', 'orange', 'red', 'blue', 'purple', 'red', 'green', 'orange']


def draw_shape(no_of_sides, color):
    for _ in range(no_of_sides):
        t.pencolor(color)
        angle = 360/no_of_sides
        t.forward(100)
        t.right(angle)


for i in range(3, 11):
    draw_shape(i, random.choice(colors))
