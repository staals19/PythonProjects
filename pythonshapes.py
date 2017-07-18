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

fillcolor("blue")

def draw_triangle():
    begin_fill()
    for i in range(3):
        right(120)
        forward(size)
    end_fill()

def foundation():
    for i in range(10):
        color = random.choice(colors)
        fillcolor(color)
        draw_triangle()
        right(30)

for i in range(10):
    foundation()
    size -= 10













# Close window on click.
exitonclick()
