import turtle
import pandas
from pandas import DataFrame

is_on = True
count = 0
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

content = pandas.read_csv('50_states.csv')
stateList = content['state'].tolist()
entered_states = []
missing_states = []


while count != len(content['state'].tolist()):
    answer_state = screen.textinput(title="States correct ({}/{})".format(count, len(content['state'].tolist())),
                                    prompt="What's another state name?").title()
    if answer_state in content['state'].tolist():
        count += 1
        entered_states.append(answer_state)
        x_value = content.loc[content.state == answer_state, 'x'].iloc[0]
        y_value = content.loc[content.state == answer_state, 'y'].iloc[0]
        t = turtle.Turtle()
        t.hideturtle()
        t.clear()
        t.penup()
        t.goto(x_value, y_value)
        t.pendown()
        t.write(answer_state)
    elif answer_state == 'Exit':
        for states in stateList:
            if states not in entered_states:
                missing_states.append(states)
        break


df = pandas.DataFrame(missing_states, columns=["Missing_States"])
csv_file_name = "missing_states.csv"

df.to_csv(csv_file_name)
