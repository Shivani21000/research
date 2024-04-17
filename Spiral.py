import turtle

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a Turtle object
spiral = turtle.Turtle()
spiral.speed(0)  # Set the speed of drawing to the fastest

# Set the initial size of the line
size = 1

# Set the number of spirals to draw
num_spirals = 500

# Draw the spiral
for _ in range(num_spirals):
    spiral.color("white")  # Set the color of the spiral
    spiral.forward(size)  # Move the turtle forward by 'size' units
    spiral.right(90)  # Turn the turtle right by 90 degrees
    size += 1  # Increase the size for the next iteration

# Hide the turtle and display the drawing
spiral.hideturtle()
turtle.done()
