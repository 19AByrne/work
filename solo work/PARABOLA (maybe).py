import turtle as t
import mpmath
import sympy
import math
# t.penup()
points = 5
length = 200
height = 350
t.speed(100)
t.color('white')
t.Screen().bgcolor('black')

for x in range(2):
    t.forward(length)
    t.right(90)
    t.forward(height)
    t.right(90)

ypoints = []
ypoints2 = []
for x in range(points):
    ypoints.append(tuple(t.pos()))
    t.forward(length/points)
    t.right(90)
    t.forward(height)
    ypoints2.append(tuple(t.pos()))
    t.backward(height)
    t.left(90)
    
vertex = tuple(t.pos())

t.backward(length)
t.right(90)

xpoints = []
for x in range(points):
    t.forward(height/points)
    xpoints.append(tuple(t.pos()))
    cachepos = t.pos()
    t.goto(vertex)
    t.goto(cachepos)
xpoints = xpoints[::-1]
xpointslines = []
for x in range(points):
    xpointslines.append(tuple((xpoints[x],vertex)))


ypointslines = []
for x in range(points):
    ypointslines.append(tuple((ypoints[x],ypoints2[x])))
    
# t.penup()
# t.color('red')
# for x in range(points):
#     t.goto(xpoints[x])
#     t.dot(5)
#     t.goto(ypoints[x])
#     t.dot(5)
#     t.goto(ypoints2[x])
#     t.dot(5)
    

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

intersections = [line_intersection((xpoints[x],vertex),(ypoints[x],ypoints2[x])) for x in range(points)]
t.goto(xpoints[0])
t.pendown()
for x in intersections:
    t.goto(x)
t.goto(vertex)