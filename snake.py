import turtle
import random
import time


width = 1000
height = 1000

#create a window
screen = turtle.Screen()
screen.setup(width, height)
screen.title("the game")
screen.bgcolor("cyan")

#create a turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")

#turtle awaits command
my_turtle.forward(100)
turtle.done()
