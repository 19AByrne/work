import turtle as t
import math
import re
import random as r
import sympy

scale = 20
t.speed(0)
t.bgcolor('black')
t.color('white')

#drawing axes
origin = (0,0)
t.forward(1000)
t.bk(2000)
t.goto(origin)
t.setheading(90)
t.forward(1000)
t.bk(2000)
t.goto(origin)

class Line:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c
        self.yint = -c/y
        self.m = (-x/y)
        self.m2 = -(1/self.m)

class Circle:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c
        self.g = (x/2)
        self.f = (y/2)
        self.centre = (-(self.g),-(self.f))
        self.r = math.sqrt((self.g)**2+(self.f)**2-c)
        
def CoefficientIntercept(equation):
    #turns string eqn into coefs. line or circle
    if not '^' in equation:
        coef_x = re.findall('-?[0-9.]*[Xx]', equation)[0][:-1]
        coef_y = re.findall('-?[0-9.]*[Yy]', equation)[0][:-1]
        intercept = re.sub("[+-]?\d+[XxYy]|[+-]?\d+\.\d+[XxYy]","", equation)
        
        return float(coef_x), float(coef_y), float(intercept)
    elif '^' in equation:
        equation = equation[7:]
        coef_x = re.findall('-?[0-9.]*[Xx]', equation)[0][:-1]
        coef_y = re.findall('-?[0-9.]*[Yy]', equation)[0][:-1]
        intercept = re.sub("[+-]?\d+[XxYy]|[+-]?\d+\.\d+[XxYy]","", equation)
        
        return float(coef_x), float(coef_y), float(intercept)
    
def Coeftoeqn(coefs,c=False):
    #given coefficients in a tuple, turns it into string of eqn. line or circle
    if c==False:
        xcoef = coefs[0]
        ycoef = coefs[1]
        const = coefs[2]
        if xcoef > 0:
            xcoef = '+'+str(xcoef)+'x'
        else:
            xcoef = str(xcoef)+'x'
        if ycoef > 0:
            ycoef = '+'+str(ycoef)+'y'
        else:
            ycoef = str(ycoef)+'y'
        if const > 0:
            const = '+'+str(const)
        else:
            const = str(const)
        return f'{xcoef}{ycoef}{const}'
    else:
        xcoef = coefs[0]
        ycoef = coefs[1]
        const = coefs[2]
        if xcoef > 0:
            xcoef = '+'+str(xcoef)+'x'
        else:
            xcoef = str(xcoef)+'x'
        if ycoef > 0:
            ycoef = '+'+str(ycoef)+'y'
        else:
            ycoef = str(ycoef)+'y'
        if const > 0:
            const = '+'+str(const)+'y'
        else:
            const = str(const)
        return f'x^2+y^2{xcoef}{ycoef}{const}'

def Angle(slope):
    return math.degrees(math.atan(slope))

def slopefrompoints(p1,p2):
    return (p2[1]-p1[1])/(p2[0]-p1[0])

def midpoint(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def perpslope(slope):
    return (-(1/slope))

def Distance2points(t,k):
    return math.sqrt((k[0]-t[0])**2+(k[1]-t[1])**2)

def drawline(l):
    #draws line, given string equation
    t.speed(0)
    coeffs = CoefficientIntercept(l)
    line = Line(coeffs[0],coeffs[1],coeffs[2])
    t.penup()
    t.goto(0,line.yint*scale)
    t.setheading(Angle(line.m))
    t.bk(1000)
    t.pendown()
    t.color('red')
    t.fd(2000)
    t.penup()
    
def simultaneous(l1,l2):
    #returns intersection, given 2 line string equations
    coef1 = CoefficientIntercept(l1)
    coef2 = CoefficientIntercept(l2)
    if not coef1[0] == coef2[0]:
        p = -coef1[0]/coef2[0]
        newcoef = [c*p for c in coef2] 
    b = coef1[1]+newcoef[1]
    c = -(coef1[2]+newcoef[2])
    y = c/b
    x = (y*coef1[1]+coef1[2])/-(coef1[0])
    return (x*scale,y*scale)

def drawcircle(c):
    #draws circle, given string equation
    t.penup()
    t.color('red')
    t.setheading(0)
    c = (CoefficientIntercept(c))
    c = Circle(c[0],c[1],c[2])
    t.goto(c.centre[0]*scale,(c.centre[1]*scale)-(c.r*scale))
    t.pendown()
    t.circle(c.r*scale)
    t.penup()


def commonct(s1,s2):
    #draws common chord/tangent, given 2 circle string eqn
    s1 = (CoefficientIntercept(s1))
    s2 = (CoefficientIntercept(s2))
    chord = (s1[0]-s2[0],s1[1]-s2[1],s1[2]-s2[2])
    chord = Coeftoeqn(chord)
    drawline(chord)
    
def linegeneral(p,m):
    #draws line, given point, given slope
    """
    y-y1=m(x-x1)
    mx-y-ma+b=0
    """
#     print((m,-1,-(m*p[0])+p[1]))
    line = (m,-1,-(m*p[0])+p[1])
    line = Coeftoeqn(line)
    drawline(line)
    
def drawcircleptc(c,k):
    #draws tangent and circle. given circle string equation, given pt of cont
    drawcircle(c)
    c = CoefficientIntercept(c)
    c = Circle(c[0],c[1],c[2])
    normal = slopefrompoints(c.centre,k)
    tanslope = perpslope(normal)
    linegeneral(k,tanslope)

def tangentfrom(c,p):
    #draws 2 tangents to a circle. given circle eqn, and outside tangent point
    c = CoefficientIntercept(c)
    c = Circle(c[0],c[1],c[2])
    m = sympy.symbols('m', real = True)
    
    #variables for perpdistance of point to line
    r = c.r
    a = m
    x1 = c.centre[0]
    b = -1
    y1 = c.centre[1]
    c = p[1]+(-1*p[0]*m)
    
    equ = sympy.Eq(r,(abs(a*x1+b*y1+c))/sympy.sqrt(a**2+b**2))
    slopes = sympy.solve(equ)
    tangent1 = linegeneral(p,slopes[0])
    tangent2 = linegeneral(p,slopes[1])
    
def circleradiuscentre(r,c):
    
               
                   
                   
                   
# circle1 = 'x^2+y^2+2x-4y-4'
# circle2 = 'x^2+y^2-4x-12y+36'
# circle3 = 'x^2+y^2-0.4x-7.2y-12.04'
# drawcircle(circle1)
# drawcircle(circle2)
# commonct(circle1,circle2)

# linegeneral((4,6),3/4)

# drawcircleptc('x^2+y^2-4x+2y-20',(5,-5))

circle = 'x^2+y^2-2x-4y-5'
outpoint = (6,11)
tangentfrom(circle,outpoint)
drawcircle(circle)

t.done()

