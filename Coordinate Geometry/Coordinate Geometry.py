import turtle as t
import math
import re
import random as r
import sympy

scale = 10
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

def Distance2points(t,k):
    return math.sqrt((k[0]-t[0])**2+(k[1]-t[1])**2)

class Triangle:
    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.g = (((p1[0]+p2[0]+p3[0])/3)*scale,((p1[1]+p2[1]+p3[1])/3)*scale)
        self.a = ((1/2)*(abs((p1[0]*(p2[1]-p3[1]))+(p2[0]*(p3[1]-p1[1]))+(p3[0]*(p1[1]-p2[1])))))*scale*scale
        self.p = (Distance2points(p1,p2)+Distance2points(p2,p3)+Distance2points(p3,p1))*scale
        self.ic = (((Distance2points(p2*scale,p3*scale))*(p1[0]*scale)) + ((Distance2points(p1*scale,p3*scale))*(p2[0]*scale)) + ((Distance2points(p1*scale,p2*scale))*(p3[0]*scale)))/((Distance2points(p2*scale,p3*scale)) + (Distance2points(p1*scale,p3*scale)) + (Distance2points(p1*scale,p2*scale))), ((Distance2points(p2*scale,p3*scale))*(p1[1]*scale) + (Distance2points(p1*scale,p3*scale))*(p2[1]*scale) + (Distance2points(p1*scale,p2*scale))*(p3[1]*scale))/((Distance2points(p2*scale,p3*scale)) + (Distance2points(p1*scale,p3*scale)) + (Distance2points(p1*scale,p2*scale)))

class Quadratic:
    def __init__(self,a,b,c):
        # k = x^2
        self.a = a
        self.b = b
        self.c = c
        self.r1 = (-(b)+math.sqrt((b)**2-(4*a*c)))/(2*a)
        self.r2 = (-(b)-math.sqrt((b)**2-(4*a*c)))/(2*a)
        self.xvertex = (-b)/(2*a)
        self.yvertex = (self.a*(self.xvertex**2)+(self.b*self.xvertex)+self.c)
        self.tp = (self.xvertex*scale,self.yvertex*scale)
        self.points = []
        for x in range(-50,50,1):
            y = ((self.a*x*x)+(self.b*x)+self.c)
            self.points.append((x*scale,y*scale))
            
def CoefficientIntercept(equation):
    #turns string eqn into coefs. line or circle
    if not '^' in equation and not 'k' in equation:
        coef_x = re.findall('-?[0-9.]*[Xx]', equation)[0][:-1]
        coef_y = re.findall('-?[0-9.]*[Yy]', equation)[0][:-1]
        intercept = re.sub("[+-]?\d+[XxYy]|[+-]?\d+\.\d+[XxYy]","", equation)
        
        return float(coef_x), float(coef_y), float(intercept)
    
    elif 'y^2' in equation:
        equation = equation[7:]
        coef_x = re.findall('-?[0-9.]*[Xx]', equation)[0][:-1]
        coef_y = re.findall('-?[0-9.]*[Yy]', equation)[0][:-1]
        intercept = re.sub("[+-]?\d+[XxYy]|[+-]?\d+\.\d+[XxYy]","", equation)
        
        return float(coef_x), float(coef_y), float(intercept)
    
    elif 'k' in equation:
        coef_x2 = re.findall('-?[0-9.]*[Kk]', equation)[0][:-1]
        coef_x = re.findall('-?[0-9.]*[Xx]', equation)[0][:-1]
        const = re.sub("[+-]?\d+[XxKk]|[+-]?\d+\.\d+[XxKk]","", equation)
        
        return float(coef_x2), float(coef_x), float(const)
    
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

def Slopefromangle(angle):
    return math.tan(math.radians(angle))

def slopefrompoints(p1,p2):
    return (p2[1]-p1[1])/(p2[0]-p1[0])

def midpoint(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)


def perpdis(p,l):
    #not sure how accurate
    l = CoefficientIntercept(l)
    return (abs((l[0]*p[0])+(l[1]*p[1])+(l[2])))/math.sqrt((l[0]**2)+(l[1]**2))

def perpslope(slope):
    if slope == 0:
        return 'Undefined'
    else:
        return (-(1/slope))



def anglebetweenlines(m1,m2):
    return math.degrees(math.atan(abs((m1-m2)/(1+m1*m2))))

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
#     t.color('red')
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
    
def linegeneral(p,m,h=False):
    #draws line, given point, given slope
    #can return string of line if hidden == True
    """
    y-y1=m(x-x1)
    mx-y-ma+b=0
    """
#     print((m,-1,-(m*p[0])+p[1]))
    if m == 'Undefined':
        line = f'1x+0y{sign(p[0])}'
        print(line)
    else:
        line = (m,-1,-(m*p[0])+p[1])
        line = Coeftoeqn(line)
    if h == False:
        drawline(line)
    else:
        return line
    
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
    
    #variables for perp distance of point to line
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
    
def sign(num):
    if num > 0:
        return f'+{num}'
    elif num < 0:
        return f'{num}'
    
def circleradiuscentre(r,c):
    #draws circle. given radius and centre
    g = (-1*c[0])
    f = (-1*c[1])
    c = -r**2+g**2+f**2
    circle = f'x^2+y^2{sign(2*g)}x{sign(2*f)}y{sign(c)}'
    t.pendown()
    drawcircle(circle)
                   
def triangle(ps):
    #draws triangle. given 3 points
    p1 = ps[0]
    p2 = ps[1]
    p3 = ps[2]
    t.penup()
    t.color('green')
    t.goto(p1[0]*scale,p1[1]*scale)
    t.pendown()
    t.goto(p2[0]*scale,p2[1]*scale)
    t.write('p2')
    t.goto(p3[0]*scale,p3[1]*scale)
    t.write('p3')
    t.goto(p1[0]*scale,p1[1]*scale)
    t.write('p1')

def centroid(ps):
    #draws centroid, given 3 points
    p1 = ps[0]
    p2 = ps[1]
    p3 = ps[2]
    t.penup()
    tri = Triangle(p1,p2,p3)
    t.goto(tri.g)
    t.color('light green')
    t.dot(6)

def bisector(p1,p2):
    #returns string equation of bisector between 2 given points
    M = midpoint(p1,p2)
    m = slopefrompoints(p1,p2)
    if m == 0:
        bisector = f'1x+0y{sign(-(M[0]))}'
        return bisector
    else:
        m = perpslope(m)
        bisector = linegeneral(M,m,True)
        return bisector
    
def circumcircle(ps):
    #draws circumcentre/circumcircle,given 3 points
    p1 = ps[0]
    p2 = ps[1]
    p3 = ps[2]
    edges = [(p1,p2),(p1,p3),(p2,p3)]
    Midpoints = [midpoint(x[0],x[1]) for x in edges]
    Slopes = [slopefrompoints(x[0],x[1]) for x in edges]
    Slopes = [perpslope(m) for m in Slopes]
    bisectors = []
    for i in edges:
        bisectors.append(bisector(i[0],i[1]))
    circumcentre = simultaneous(bisectors[0],bisectors[1])
    t.goto(circumcentre)
    t.color('red')
    t.dot(5)
    circumcentre = (circumcentre[0]/scale,circumcentre[1]/scale)
    r = Distance2points((circumcentre),(p1[0],p1[1]))
    circleradiuscentre(r,circumcentre)
    
def incircle(ps):
    #draws incircle/incentre, given 3 points
    p1 = ps[0]
    p2 = ps[1]
    p3 = ps[2]
    tri = Triangle(p1,p2,p3)
    incentre = tri.ic
    r = (2*tri.a)/tri.p
    t.color('dark violet')
    t.goto(incentre)
    t.dot(5)
    circleradiuscentre(r/scale,(incentre[0]/scale,incentre[1]/scale))

def quadratic(eqn):
    t.color('yellow')
    t.penup()
    eqn = CoefficientIntercept(eqn)
    eqn = Quadratic(eqn[0],eqn[1],eqn[2])
    t.goto(eqn.r1*scale,0)
    t.dot(5)
    t.goto(eqn.r2*scale,0)
    t.dot(5)
    t.goto(eqn.tp)
    t.dot(5)
    t.goto(eqn.points[0])
    t.pendown()
    for p in eqn.points:
        t.goto(p)
        
def polynomial(eqn):
    pass
    
    
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

# circleradiuscentre(10,(-2,2))

# mytriangle = ((-23,-3),(-35,35),(12,3))
# p1 = (r.randint(-30,30), r.randint(-30,30))
# p2 = (r.randint(-30,30), r.randint(-30,30))
# p3 = (r.randint(-30,30), r.randint(-30,30))
# print(p1,p2,p3)
# mytriangle = (p1,p2,p3)
# triangle(mytriangle)
# centroid(mytriangle)
# circumcircle(mytriangle)
# incircle(mytriangle)

# qd = Quadratic(-2,-4,6)
# print(qd.xvertex)
# print(qd.yvertex)

# quadratic('1k-1x-12')

# polynomial(ply)




t.done()

