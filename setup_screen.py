import turtle

def setup_screen(title="Program", lenx=640, leny=320, \
    background="white", tracer_size=800):
    """Sets up the turtle window. Required to run the main script
    title - the title of the program window
    lenx - horizontal pixel length of window
    leny - vertical pixel length of window
    background - background colour of the screen
    tracer_size - amount of actions completed in memory before updating to screen
    """
    print("Setting up screen")

    turtle.title(title)
    turtle.setup(lenx, leny, starty=leny/2)
    turtle.hideturtle()
    turtle.penup()
    turtle.backward(240)
    # Makes rendering faster by completing multiple actions in
    # memory before rendering
    turtle.tracer(tracer_size)  
    turtle.bgcolor(background)
    print("Screen setup finished")
