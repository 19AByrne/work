#turtle exercise 66
import random
import turtle
t = turtle
r = random
colours = ["pink", "brown", "purple", "blue", "red", "orange", "gray", "black"]

def octogonline(clr):
    t.color(clr)
    t.forward(50)
    t.left(45)
for x in range(8):
    colour = r.choice(colours)
    colours.pop(colours.index(colour))
    octogonline(colour)