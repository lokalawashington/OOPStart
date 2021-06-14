#import turtle
"""check docs.python.org/library/turtle.html for more methods."""
import turtle

import another_module
from turtle import Turtle, Screen

#print(another_module.another_variable)
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(200)

my_screen = Screen()
print(my_screen.canvheight)

#method exitonclick()
my_screen.exitonclick()


