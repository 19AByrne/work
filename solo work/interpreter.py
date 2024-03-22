import turtle as t
import math
import re

t.speed(10)
t.bgcolor('black')
t.color('white')
class Line:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c
        self.yint = (0,-c/y)
        self.slope = (-x/y)
        
l1 = '-0.93x+8.27y-3.8'
numberlist = ['1','2','3','4','5','6','7','8','9','0']
def CoefficientIntercept(equation):
    coef_x = re.findall('-?[0-9.]*[Xx]', equation)[0][:-1]
    coef_y = re.findall('-?[0-9.]*[Yy]', equation)[0][:-1]
    intercept = re.sub("[+-]?\d+[XxYy]|[+-]?\d+\.\d+[XxYy]","", equation)
    
    return float(coef_x), float(coef_y), float(intercept)

l1 = [CoefficientIntercept(l1)]
l1 = l1[0]
line2 = Line(l1[0],l1[1],l1[2])
slope = line2.slope
angle = math.degrees(math.atan(slope))
print(line2.yint)


origin = (0,0)
t.forward(1000)
t.bk(2000)
t.goto(origin)
t.setheading(90)
t.forward(1000)
t.bk(2000)

t.goto(line2.yint)
t.color('red')
t.setheading(angle)
t.fd(1000)
t.bk(2000)

    
    
