#turtle exercise 63
import turtle
t = turtle
import random
r = random
colours = ['red', 'black', 'purple']
def square():
    t.color = ('black', r.choice(colours))
    for x in range(4):
        t.forward(100)
        t.left(90)
square()