import turtle

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
