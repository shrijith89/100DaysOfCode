import turtle
import pandas

is_on = True
count = 0
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?").title()
content = pandas.read_csv('50_states.csv')
length_of_content = len(content['state'].tolist())

while count != length_of_content:
    if answer_state not in content['state'].tolist():
        pass
    else:
        count += 1
        x_value = content.loc[content.state == answer_state, 'x'].iloc[0]
        y_value = content.loc[content.state == answer_state, 'y'].iloc[0]
        t = turtle.Turtle()
        t.hideturtle()
        t.clear()
        t.penup()
        t.goto(x_value, y_value)
        t.pendown()
        t.write(answer_state)
    answer_state = screen.textinput(title="States correct ({}/{})".format(count, len(content['state'].tolist())), prompt="What's another state name?").title()

print("Game complete")

screen.exitonclick()
