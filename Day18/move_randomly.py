import turtle as t
import random


def move_random(j):
    for _ in range(100):
        if j == 0:
            t.forward(60)
            t.right(90)
        else:
            t.forward(40)
            t.left(70)


r = [0, 1]

for i in range(50):
    move_random(random.choice(r))
