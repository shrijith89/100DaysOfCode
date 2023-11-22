import colorgram
import turtle as t

colors = colorgram.extract('spot_painting.jpg', 25)
color_list = []

for i in range(len(colors)):
    color_list.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))


def draw_dots():
    t.colormode(255)
    for i in range(9):
        t.setx(0)
        t.sety(t.ycor()+40)
        for j in range(len(color_list)-5):
            t.pencolor(color_list[j])
            t.dot(20)
            t.penup()
            t.forward(30)


draw_dots()
