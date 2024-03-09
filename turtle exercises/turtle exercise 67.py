#turtle exercise 67
import turtle
t = turtle
def octogon():
    for x in range(8):
        t.forward(50)
        t.right(45)
        
for x in range(12):
    octogon()
    t.right(30)