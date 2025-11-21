import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


df = pd.read_csv("50_states.csv")
states = df["state"].tolist()

def coordinates(state_name):
    row = df[df["state"] == state_name]
    x = int(row.x.iloc[0]) - 18
    y = int(row.y.iloc[0])

    return x, y


GAME_ON = True
counter = 0

while GAME_ON:
    answer_state = screen.textinput(title=f"Guessed States {counter}/50", prompt="Guess next state name:")
    if type(answer_state) is str:
        state = answer_state.title()
    else:
        state = "a"
    if state in states:
        counter += 1
        states.remove(state)

        (X, Y) = coordinates(state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(X, Y)
        t.write(state, font=("Arial", 8, "normal"))

    elif state == "Exit":
        break


    if counter >= 50:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(-175, 0)
        t.write("YOU WON", font=("Arial", 50, "normal"))

        GAME_ON = False


# csv file of states not guessed by user:
data_frame = df = pd.DataFrame(states, columns=["not guessed states"])
data_frame.to_csv("not_guessed_states.csv")



# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

