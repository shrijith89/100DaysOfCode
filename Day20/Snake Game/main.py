from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
color = ['red', 'green', 'blue']
is_on = True
screen.tracer(0)

snake = Snake()

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
