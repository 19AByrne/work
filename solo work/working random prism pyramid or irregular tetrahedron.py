import turtle
import random
import time
turtle.bgcolor('black')
turtle.color('white')
def prism():
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    t1.color('white')
    t1.hideturtle()
    t2.color('white')
    t2.hideturtle()
    t3.color('white')
    t3.hideturtle()
    r = random
    lines = r.randint(3,10)
    angle = 360/lines
    length = r.randint(25,150)
    offset = r.randint(0,360)
    extrusion = r.randint(25,175)
    projection = r.randint(0,360)
    t1.speed(10)
    t2.speed(10)
    t3.speed(10)

    t1.left(offset)
    t2.left(offset)
    t3.left(offset)

    def turt1():
        for x in range(lines):
            t1.forward(length)
            t1.left(angle)
            
    def turt2():   
        for x in range(lines):
            t2.forward(length)
            t2.left(angle)
            t2.right(offset+(angle*x))
            t2.left(projection)
            t2.forward(extrusion)
            t2.backward(extrusion)
            t2.right(projection)
            t2.left(offset+(angle*x))
            
    def turt3():
        t3.forward(length) 
        t3.right(offset)
        t3.left(angle+projection)
        t3.forward(extrusion)
        t3.right(angle+projection)
        t3.left(angle+offset)
        for x in range(lines):
            t3.forward(length)
            t3.left(angle)
            
    form = ['turt1', 'turt2', 'turt3']
    r.shuffle(form)

    for x in range(3):
        if form[x] == 'turt1':
            turt1()
        elif form[x] == 'turt2':
            turt2()
        elif form[x] == 'turt3':
            turt3()
    time.sleep(0.7)
    turtle.Screen().reset()
            
def pyramid():
    r= random
    t=turtle
    t.color('white')
    t.hideturtle()
    t.speed(5)
    lines = r.randint(3,10)
    length = r.randint(1,200)
    angle = 360/lines
    offset = r.randint(0,360)
    offsetdis = r.randint(-90,90)
    ver = (r.randint(-250,250),r.randint(-250,250))
    t.penup()
    t.left(offset)
    t.forward(offsetdis)
    t.pendown()
    for x in range(lines):
        t.forward(length)
        t.left(angle)
        pos = t.pos()
        t.goto(ver)
        t.goto(pos)
    time.sleep(0.7)
    turtle.Screen().reset()

def rtetra():
    r=random
    t = turtle
    t.color('white')
    t.hideturtle()
    p1 = (r.randint(1,300),r.randint(1,300))
    p2 = (r.randint(1,300),r.randint(1,300))
    p3 = (r.randint(1,300),r.randint(1,300))
    ver = (r.randint(1,300),r.randint(1,300))
    path = [p1, p2, p3, p1, ver, p2, p3, ver]
    t.penup()
    t.goto(p1)
    t.pendown()
    for x in range(len(path)):
        t.goto(path[x])
    time.sleep(0.7)
    turtle.Screen().reset()
while 1 == 1:      
    option = random.randint(1,4)
    if option == 1:
        prism()
        
    elif option == 2:
        pyramid()
        
    elif option == 3:
        rtetra()
        



