#turtle exercise 63
import turtle
t = turtle
import random
r = random
x = 0
y = 0
colours = ["orange", "red", "purple", "blue", "green", "pink"]

def square(x,y,clr):
    t.goto(x,y)
    t.pendown()
    t.fillcolor(clr)
    t.begin_fill()
    for x in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()
    t.penup()
colour = r.choice(colours)
square(x,y, colour)
colour = r.choice(colours)
square(x+105,y, colour)
colour = r.choice(colours)
square(x+210,y, colour)

