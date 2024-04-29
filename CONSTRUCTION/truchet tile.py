import turtle as t
import math as m
import random as r
t.bgcolor('black')
t.color('white')
t.speed(0)

sl = 15
ph = (sl*2)*m.sin(m.pi/3)


def hexagon():
    i = r.choice((0,1,2))
    t.pendown()
    vs = []

    for x in range(6):
        vs.append(t.pos())
        t.forward(sl)
        t.left(60)

    t.penup()
    t.goto(vs[i])
    t.setheading((i)*60)

    t.pendown()
    t.forward(sl/2)
    t.left(90)
    t.circle(sl/2,120)

    i2 = i + 3
    t.penup()
    t.goto(vs[i2])
    t.setheading((i2)*60)

    t.pendown()
    t.forward(sl/2)
    t.left(90)
    t.circle(sl/2,120)

    t.penup()
    i3 = i + 1
    t.goto(vs[i3])
    t.setheading((i3)*60)

    t.pendown()
    t.forward(sl/2)
    t.left(90)
    t.forward(ph)
    
    t.penup()
    t.goto(vs[2])
    t.setheading(0)
    
while True:
    origin = t.pos()
    for x in range(10):
        hexagon()
    t.goto(origin)
    t.penup()
    t.right(90)
    t.forward(ph)
    t.setheading(0)
    