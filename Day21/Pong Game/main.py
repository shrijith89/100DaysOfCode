from turtle import Turtle, Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Use the instance 'paddle' to access the methods
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


screen.tracer(0)
screen.listen()

game_is_on = True

while game_is_on:
    time.sleep(0.009)

    screen.update()



screen.exitonclick()
