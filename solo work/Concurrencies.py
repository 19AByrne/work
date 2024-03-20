import turtle as t
import random as r
import math

t.bgcolor('black')
t.color('white')
t.speed(10)
t.hideturtle()

rg = 250

# A = ((r.randint(-rg,rg)),(r.randint(-rg,rg)))
# B = ((r.randint(-rg,rg)),(r.randint(-rg,rg)))
# C = ((r.randint(-rg,rg)),(r.randint(-rg,rg)))
A = (100,-100)
B = (-150,-150)
C = (0,80)
ps = [A,B,C]

t.penup()
t.goto(ps[-1])
pointsnames = ['A','B','C']
for i,p in enumerate(ps):
    t.pendown()
    t.goto(p)
    t.dot(6)
    t.write(pointsnames[i])
    
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
    pass

def Distance2points(t,k):
    return math.sqrt((k[0]-t[0])**2+(k[1]-t[1])**2)

def DrawCentroid():
    Midpoints = []
    Midpoints.append(Midpoint(A,B))
    Midpoints.append(Midpoint(A,C))
    Midpoints.append(Midpoint(C,B))
    t.penup()
    t.goto(Midpoints[0])
    t.dot(5)
    t.pendown()
    t.goto(C)
    t.penup()
    t.goto(Midpoints[1])
    t.dot(5)
    t.pendown()
    t.goto(B)
    t.penup()
    t.goto(Midpoints[2])
    t.dot(5)
    t.pendown()
    t.goto(A)
    t.penup()
    G = Centroid(A,B,C)
    t.goto(G)
    t.color('light green')
    t.dot(10)


def DrawCircum():
    t.penup()
    distances = [Distance2points(A,B),Distance2points(A,C),Distance2points(C,B)]
    Midpoints = [Midpoint(A,B),Midpoint(A,C),Midpoint(C,B)]
    slopes = [Slope(A,B),Slope(A,C),Slope(C,B)]
    slopes = [PerpendicularSlope(x) for x in slopes]
    slopes = [Angle(x) for x in slopes]
    Bisectors = []

    t.goto(Midpoints[0])
    # t.pendown()
    t.setheading(slopes[0])
    t.forward(distances[0])
    p1 = t.pos()
    t.bk(distances[0]*2)
    p2 = t.pos()
    Bisectors.append((p1,p2))
    t.penup()

    t.goto(Midpoints[1])
    # t.pendown()
    t.setheading(slopes[1])
    t.forward(distances[1])
    p1 = t.pos()
    t.bk(distances[1]*2)
    p2 = t.pos()
    Bisectors.append((p1,p2))
    t.penup()

    t.goto(Midpoints[2])
    # t.pendown()
    t.setheading(slopes[2])
    t.forward(distances[2])
    p1 = t.pos()
    t.bk(distances[2]*2)
    p2 = t.pos()
    Bisectors.append((p1,p2))
    t.penup()

    circumcentre = line_intersection(Bisectors[0],Bisectors[1])
    t.goto(circumcentre)
    t.color('red')
    t.dot(10)

    radius = Distance2points(circumcentre,A)
    TheSlope = Slope(circumcentre,A)
    t.goto(A)
    TheSlope = PerpendicularSlope(TheSlope)
    TheAngle = Angle(TheSlope)
    t.setheading(TheAngle)
    t.pendown()
    t.circle(radius)

# DrawCentroid()
# DrawCircum()

def anglebetween(m1,m2):
    return math.degrees(math.atan((m1-m2)/1+(m1)*(m2)))
"""
slope of CB = angle of a
slope of AC = angle of 
# slopes = [Slope(C,B),Slope(A,C),Slope(A,B)]
"""
# Angles = [anglebetween(

