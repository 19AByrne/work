import turtle as t
import random as r
import math

t.bgcolor('black')
t.color('white')
t.speed(10)

rg = 250

A = ((r.randint(-rg,rg)),(r.randint(-rg,rg)))
B = ((r.randint(-rg,rg)),(r.randint(-rg,rg)))
C = ((r.randint(-rg,rg)),(r.randint(-rg,rg)))
ps = [A,B,C]

t.penup()
t.goto(ps[-1])
for p in ps:
    t.pendown()
    t.goto(p)
    t.dot(6)
    
def Midpoint(t,k):
    return ((t[0]+k[0])/2,(t[1]+k[1])/2)

def Centroid(t,k,j):
    return ((t[0]+k[0]+j[0])/3,(t[1]+k[1]+j[1])/3)

def Slope(t,k):
    return (k[1]-t[1])/(k[0]-t[0])

def PerpendicularSlope(slope):
    return (-(1/slope))

def Angle(slope):
    return math.degrees(math.atan(slope))

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def Mediator(slope,midpoint):
    