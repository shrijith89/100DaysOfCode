import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
pen = turtle.Turtle()

# Function to write text
def write_text():
    # Move the turtle to a specific position
    x_position = turtle.numinput("Input", "Enter X position:")
    y_position = turtle.numinput("Input", "Enter Y position:")
    pen.penup()
    pen.goto(x_position, y_position)
    pen.pendown()

    # Get text input from the user
    text = turtle.textinput("Input", "Enter text to write:")

    # Write the text at the specified position
    pen.write(text, align="center", font=("Arial", 16, "normal"))

# Bind the function to a key press event
screen.listen()
screen.onkey(write_text, "w")

# Keep the window open
turtle.done()
