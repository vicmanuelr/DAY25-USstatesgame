import turtle
import pandas as pd

# Setup of a U.S. map image on the turtle screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=730, height=496, startx=500, starty=-250)
turtle.shape(image)


# # getting coordinates from the screen with us map
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
# # with this code made 50_states.csv coordinates with this method


write_turtle = turtle.Turtle()  # Turtle that will write answers on map
write_turtle.hideturtle()
list_of_answers = []  # List to check if answer is already given
data = pd.read_csv("50_states.csv")


def valid_answer(user_answer, previous_ans, game_data):
    if user_answer in previous_ans:
        return False
    state_data = game_data[game_data.state == user_answer]
    states_list = game_data.state.to_list()
    if user_answer in states_list:
        x_cor = float(state_data.x)
        y_cor = float(state_data.y)
        write_turtle.penup()
        write_turtle.goto(x_cor, y_cor)
        write_turtle.write(user_answer, align="left")
        previous_ans.append(user_answer)
        return True


# Getting user input for game
game_is_on = True
while game_is_on:
    user_input = screen.textinput(title="Guess the State", prompt="What's another state name:")
    if user_input is None or user_input == "exit":
        game_is_on = False
        break
    else:
        user_input = user_input.title()
    if valid_answer(user_input, list_of_answers, data):
        screen.title(f"You got {len(list_of_answers)}/50")
    if len(list_of_answers) == 50:
        game_is_on = False

states_to_learn = sorted(list(set(data["state"].to_list()) - set(list_of_answers)))
pd.DataFrame(states_to_learn).to_csv("states_to_learn.csv")

screen.exitonclick()
