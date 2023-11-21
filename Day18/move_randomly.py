import turtle as t
import random

colors = ['blue', 'yellow', 'red', 'black', 'brown']
t.pensize(10)
t.speed("fastest")
screen = t.Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_combo = (r, g, b)
    return color_combo


def move_random():
    t.colormode(255)
    for _ in range(100):
        t.pencolor(random_color())
        t.forward(25)
        t.setheading(random.choice(range(0, 360, 90)))


move_random()
