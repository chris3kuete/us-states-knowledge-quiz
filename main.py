import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# screen.exitonclick()

data = pandas.read_csv("50_states.csv")
state_toList = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name ?").capitalize()

    if answer_state in state_toList:
        guessed_states.append(answer_state)
        tu = turtle.Turtle()
        tu.hideturtle()
        tu.penup()
        row_state = data[data.state == answer_state]  # THIS WILL PULL OUT THE ROW WHERE THE STATE IS EQUAL TO GUESSED STATE
        tu.goto(int(row_state.x), int(row_state.y))
        tu.write(row_state.state.item())  # WE CAN ALSO JUST USE ANSWER_STATE1 #ITEM() IS A METHOD IN THE PANDA SERIES THAT RETURN THE FIRST ELEMENT OF THE UNDERLYING DATA

    if answer_state == "Exit":
        missing_states = []
        missing_states = [s for s in state_toList if s not in guessed_states]
        #for s in state_toList:
            #if s not in guessed_states:
                #missing_states.append(s)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break




