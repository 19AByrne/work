#cylinder
import turtle
import random
t = turtle
r = random
def cylinder()
    rad = r.randint(40,100)
    t.circle(rad)
    offset = r.randint(0,360)
    extrusion = r.randint(30,300)
    t.penup()
    t.left(90)
    t.forward(rad)
    t.right(90)
    t.right(offset)
    mid = t.pos()
    t.forward(rad)
    t.right(90)
    projangle = t.heading()
    p1 = t.pos()
    t.goto(mid)
    t.right(90)
    t.forward(rad)
    t.setheading(projangle)
    p2 = t.pos()
    t.pendown()
    t.forward(extrusion)
    t.penup()
    t.goto(p1)
    t.pendown()
    t.setheading(projangle)
    t.forward(extrusion)
    t.right(180)
    t.circle(rad)
    time.sleep(0.7)
    turtle.Screen().reset()
