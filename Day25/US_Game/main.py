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
    if answer_state not in content['state'].tolist():
        print("Not found")
        is_on = False
    else:
        x_value = content.loc[content.state == answer_state, 'x'].iloc[0]
        y_value = content.loc[content.state == answer_state, 'y'].iloc[0]
        turtle.clear()
        turtle.penup()
        turtle.goto(x_value, y_value)
        turtle.pendown()
        turtle.write(answer_state)

screen.exitonclick()
