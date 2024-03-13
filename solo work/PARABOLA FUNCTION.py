import turtle as t
import mpmath
import sympy
import math
import time

points = 5
length = 200
height = 350
t.speed(10)
t.color('white')
t.Screen().bgcolor('black')
t.hideturtle()


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

def drawline(line):
    t.penup()
    t.goto(line[0])
    t.pendown()
    t.goto(line[1])
    t.penup()
    

def parabola(p,h,l,dl,c):
    t.backward(l)
    for x in range(2):
        t.forward(l*2)
        t.left(90)
        t.forward(h)
        t.left(90)
    
    vertex = (0,height)
    fracl = (l/p)
    frach = (h/p)
    
    ypoints = []
    ypoints2 = []
    for x in range(1,p+1):
        ypoints.append((-(fracl*x),0))
        ypoints2.append((-(fracl*x),h))
        
    xpoints = []
    for x in range(p):
        xpoints.append((-(l),frach*x))
        
    xlines = []
    ylines = []
    for x in range(p):
        xlines.append((xpoints[x],vertex))
        ylines.append((ypoints[x],ypoints2[x]))
    xlines=xlines[::-1]
    
    if dl == True:
        for i in range(p):
            drawline(xlines[i])
            drawline(ylines[i])
        
    intersections = []
    for x in range(p):
        intersections.append(line_intersection(xlines[x],ylines[x]))
    intersections1 = intersections[::-1]
    intersections2 = [((x[0])*-1,(x[1])) for x in intersections]
    
    t.color(c)
    for x in intersections1:
        t.goto(x)
        t.pendown()
    t.goto(vertex)
    for x in intersections2:
        t.goto(x)
        
    t.done()
points = int(input("Enter amount of points: "))
length = 200
height = 350
colour = str(input("Enter Colour: "))
drawlines = str(input("Do you want to see contruction lines? (y/n)\n"))
if drawlines == 'y':
    drawlines == True
else:
    drawlines == False

parabola(points,height,length,drawlines,colour)
