import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
color = ['red', 'green', 'blue']
is_on = True
screen.tracer(0)

snake = Snake()
food = Food()
score = scoreboard.Scoreboard()

screen.listen()
turtle.onkey(snake.up, 'Up')
turtle.onkey(snake.down, 'Down')
turtle.onkey(snake.right, 'Right')
turtle.onkey(snake.left, 'Left')

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.randomize_food()

screen.exitonclick()
