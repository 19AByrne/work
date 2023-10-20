import turtle
t = turtle
xs = 500
ys = 10
t.speed(10)
for x in range(50):
    t.goto(0,0)
    t.backward(xs)
    t.goto(0,ys)
    xs -= 10
    ys += 10
for x in range(100):
    t.goto(0,0)
    t.forward(xs)
    t.goto(0,ys)
    xs += 10
    ys -= 10
for x in range(100):
    t.goto(0,0)
    t.backward(xs)
    t.goto(0,-ys)
    xs -= 10
    ys += 10
for x in range(100):
    t.goto(0,0)
    t.forward(xs)
    t.goto(0,-ys)
    xs += 10
    ys -= 10    
    
    
    
    
t.done()