import turtle
import random

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
r = random
lines = r.randint(3,10)
angle = 360/lines
length = r.randint(25,150)
offset = r.randint(0,360)
extrusion = r.randint(25,175)
projection = r.randint(0,360)
t1.speed(10)
t2.speed(10)
t3.speed(10)

t1.left(offset)
t2.left(offset)
t3.left(offset)

def turt1():
    for x in range(lines):
        t1.forward(length)
        t1.left(angle)
        
def turt2():   
    for x in range(lines):
        t2.forward(length)
        t2.left(angle)
        t2.right(offset+(angle*x))
        t2.left(projection)
        t2.forward(extrusion)
        t2.backward(extrusion)
        t2.right(projection)
        t2.left(offset+(angle*x))
        
def turt3():
    t3.forward(length) 
    t3.right(offset)
    t3.left(angle+projection)
    t3.forward(extrusion)
    t3.right(angle+projection)
    t3.left(angle+offset)
    for x in range(lines):
        t3.forward(length)
        t3.left(angle)
        
form = ['turt1', 'turt2', 'turt3']
r.shuffle(form)

for x in range(3):
    if form[x] == 'turt1':
        turt1()
    elif form[x] == 'turt2':
        turt2()
    elif form[x] == 'turt3':
        turt3()
