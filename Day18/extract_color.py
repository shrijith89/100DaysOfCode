import colorgram
import turtle as t
import random

colors = colorgram.extract('spot_painting.jpg', 25)
color_list = []

for i in range(len(colors)):
    color_list.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))


def draw_dots():
    t.colormode(255)
    for i in range(10):
        for j in range(len(color_list)-15):
            t.dot(20, random.choice(color_list))
            t.penup()
            t.forward(50)
        t.sety(t.ycor() + 40)
        t.setx(0)


draw_dots()
