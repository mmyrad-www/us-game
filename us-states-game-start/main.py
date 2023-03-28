import turtle
import pandas

game_continues = True
score = 0
screen = turtle.Screen()
screen.title("USA States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


data = pandas.read_csv("50_states.csv")

states = data["state"].to_list()

while len(states)!=0:
    answer_state = screen.textinput(title=f"{score}/50 states are correct!", prompt="What's another state's name?").title()
    if answer_state=="Exit":
        print(states)
        break
    if answer_state in states:
        timmy=turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_data=data[data.state==answer_state]
        timmy.goto(int(state_data.x),int(state_data.y))
        timmy.write(answer_state)
        score += 1

        states.remove(answer_state)
    else:
        pass


