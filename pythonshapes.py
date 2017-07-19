from turtle import *
import math
import turtle, random

# Name your Turtle.
t = Turtle()
colors = ["red","green","blue","orange","purple","pink","yellow"]

# Set Up your screen and starting position.
setup(500,300)
penup()
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

#size = input('How big do you want your shape to be?')
pendown()

#for i in range(4):
    #forward(50)
    #right(90)

penup()
#forward(200)
pendown()

size = 100
sides = input("How many sides?")
sides = int(sides)
#colors = str(colors)
color = input("What color?")


while color not in colors:
    color = input("What color?")


print(sides)

fillcolor(color)

def draw_shape():
    begin_fill()
    for i in range(sides):
        right(360/sides)
        forward(size)
    end_fill()

draw_shape()

'''def foundation():
    for i in range(10):
        color = random.choice(colors)
        fillcolor(color)
        draw_triangle()
        right(30)

#for i in range(10):
    #foundation()
    #size -= 10'''













# Close window on click.
exitonclick()

