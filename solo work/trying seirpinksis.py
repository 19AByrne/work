import turtle
import random
t = turtle
t.speed(10)
def point_on_triangle(pt1, pt2, pt3):
    """
    Random point on the triangle with vertices pt1, pt2 and pt3.
    """
    x, y = sorted([random.random(), random.random()])
    s, t, u = x, y - x, 1 - y
    return (s * pt1[0] + t * pt2[0] + u * pt3[0],
            s * pt1[1] + t * pt2[1] + u * pt3[1])

# t.penup()
# t.hideturtle()
for x in range(3):
    t.forward(400)
    t.left(120)


p1 = t.pos()
t.forward(400)
p2 = t.pos()
t.left(120)
t.forward(400)
p3 = t.pos()


t.goto(point_on_triangle(p1,p2,p3))
points = [p1,p2,p3]
selected = random.choice(points)
rpos = t.pos()
