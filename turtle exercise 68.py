#turtle exercise 68
import turtle
import random
t = turtle
r = random
print("---RANDOM SHAPE---")
yn = str(input("Do you want your shape to be connected?\n'y' for yes, 'n' for no\n"))
if yn == 'y':
    lines = r.randint(3,20)
    length = r.randint(20,100)
    angle = 360/lines
    for x in range(lines):
        t.forward(length)
        t.left(angle)
elif yn == 'n':
    for x in range(r.randint(1,20)):
        t.forward(r.randint(20,100))
        lr = r.randint(1,2)
        if lr == '1':
            t.right(r.randint(1,360))
        else:
            t.left(r.randint(1,360))
        
