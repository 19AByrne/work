#octahedron
import turtle
import random
r = random
t = turtle
t.speed(2)
mid = t.pos()
t.penup()
t.dot(5)
offset = r.randint(0,360)
length = r.randint(100,300)
t.right(offset)
t.forward(length)
t.dot(5)
t.goto(mid)
t.backward(length)
t.dot(5)
t.goto(mid)
t.pendown()
t.right(90)
t.forward(length)





t.done