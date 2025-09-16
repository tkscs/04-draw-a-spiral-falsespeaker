import turtle
from scipy.constants import golden as phi
"""
Make a rectangular spiral (see the README.md for an example)
"""

### YOUR CODE STARTS HERE
turtle.speed(1000)
for i in range(100):
    turtle.forward(phi*i)
    turtle.right(90)
### YOUR CODE ENDS HERE

turtle.exitonclick()