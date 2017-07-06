from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(400,200)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:
for i in range(4):
    forward(50)
    right(90)


# Close window on click.
exitonclick()
