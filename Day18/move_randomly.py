import turtle as t
import random

colors = ['blue', 'yellow', 'red', 'black', 'brown']


def move_random():
    for _ in range(100):
        t.pencolor(random.choice(colors))
        t.pensize(10)
        t.forward(25)
        t.right(random.choice(range(0, 360, 90)))


move_random()
