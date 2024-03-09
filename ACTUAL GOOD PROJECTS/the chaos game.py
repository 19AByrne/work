import turtle
import random
import time
t = turtle
t.speed(10)
t.Screen().bgcolor('black')
t.color('white')
t.hideturtle()
def point_on_triangle(pt1, pt2, pt3):
    """
    Random point on the triangle with vertices pt1, pt2 and pt3.
    """
    x, y = sorted([random.random(), random.random()])
    s, t, u = x, y - x, 1 - y
    return (s * pt1[0] + t * pt2[0] + u * pt3[0],
            s * pt1[1] + t * pt2[1] + u * pt3[1])
t.penup()

p1 = t.pos()
t.forward(400)
p2 = t.pos()
t.left(120)
t.forward(400)
p3 = t.pos()

points = [p1,p2,p3]
ranpos = point_on_triangle(p1,p2,p3)
while 1==1:
    selected = random.choice(points)
    midx = (selected[0]+ranpos[0])/2
    midy = (selected[1]+ranpos[1])/2
    midpoint = (midx,midy)
    t.goto(midpoint)
    t.dot(2)
    ranpos = midpoint