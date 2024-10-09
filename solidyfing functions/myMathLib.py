import math
def circle_area(diameter):
    r = diameter/2
    return ((diameter/2)**2)*math.pi

def rectangle_area(h,w):
    return h*w

def perimeter_circle(diameter):
    return 2*math.pi*(diameter/2)

def rectangle_perimeter(h,w):
    return 2*h+2*w