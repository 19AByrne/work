#penrose triangle
import turtle
import random
r=random
t=turtle
t.speed(10)
lines = r.randint(3,6)
angle = (360/lines)
length = r.randint(50,100)
difference = (length/4)
nextlength = (length+difference)
longestlength = (length+((length/10)*7))
connectdistance = (angle/3)
connectangle = (angle/4.8)
for x in range(lines):
    t.forward(length)
    t.left(angle)
for x in range(lines):
    t.forward(nextlength)
    t.backward(difference)
    t.left(angle)
for x in range(lines):
    t.forward(nextlength)
    t.left(angle)
    t.forward(longestlength)
    t.backward(longestlength)
    t.left(angle/2)
    t.forward(difference)
    t.right(angle/2)
    
for x in range(lines):
    t.forward(nextlength)
    t.left(angle)
    t.forward(longestlength)
    t.left(angle)
    t.forward(longestlength)
    t.left(25)
    t.forward(40)
    
    t.backward(40)
    t.right(25)
    t.backward(longestlength)
    t.right(angle)
    t.backward(longestlength)
    t.right(angle)
    t.backward(difference)
    
    t.left(angle)
    
    







