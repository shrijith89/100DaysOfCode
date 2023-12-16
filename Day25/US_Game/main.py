import turtle
import pandas

is_on = True

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?").title()
    content = pandas.read_csv('50_states.csv')
    valuex = content.loc[content.state == answer_state, 'x'].iloc[0]
    valuey = content.loc[content.state == answer_state, 'y'].iloc[0]
    turtle.penup()
    turtle.goto(valuex, valuey)
    turtle.write(answer_state)

screen.exitonclick()
