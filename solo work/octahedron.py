#octahedron
import turtle
import random
import time
r = random
t = turtle
while 1==1:
    t.speed(10)
    offset = r.randint(0,360)
    length = r.randint(75,200)
    lines = 4
    points = []
    t.left(offset)
    t.penup()
    for x in range(lines):
        t.forward(length)
        points.append(t.pos())
        t.left(360/lines)

    v1 = points[0]
    v2 = points[2]
    midx = (v1[0]+v2[0])/2
    midy = (v1[1]+v2[1])/2
    mid = (midx,midy)

    t.goto(mid)

    bpdis = r.randint(20,60)
    bpdis = (length/100)*bpdis

    bpdis2 = r.randint(20,60)
    bpdis2 = (length/100)*bpdis2

    t.right(45)
    t.forward(bpdis/2)
    t.left(90)
    t.forward(bpdis2/2)
    p1 = t.pos()

    t.goto(mid)
    t.left(90)
    t.forward(bpdis/2)
    t.left(90)
    t.forward(bpdis2/2)
    p2 = t.pos()


    t.pendown()
    for x in range(len(points)):
        t.goto(points[x])
        t.goto(p2)
        
    t.penup()
    t.goto(p1)
    t.pendown()
    for x in range(len(points)):
        t.goto(points[x])
        t.goto(p1)
        
    t.penup()
    t.goto(points[-1])
    t.pendown()
    for x in range(len(points)):
        t.goto(points[x])
    t.penup()
    time.sleep(1)
    turtle.Screen().reset()
    

t.done()
