import turtle as t
from pynput import keyboard
s = t.Screen()
t.bgcolor('black')
t.color('white')
def up():
    t.setheading(90)
    t.forward(100)

def down():
    t.setheading(270)
    t.forward(100)
    
def left():
    t.setheading(180)
    t.forward(100)
    
def right():
    t.setheading(0)
    t.forward(100)

def dot():
    t.dot(5)

with keyboard.Events() as events:
    for event in events:
        if event.key== keyboard.Key.esc:
            print('wamp')
        else:
            print('w')
