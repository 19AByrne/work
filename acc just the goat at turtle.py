#turtle testing
import turtle
cmove = 0
moves = int(input("How many moves do you want to make?\n"))
def goright():
    turtle.forward(100)   
def goleft():
    turtle.backward(100)  
def goup():
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)    
def godown():
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
def savepoint():
    corx = turtle.xcor()
    cory = turtle.ycor()
    return cory,corx
path = []
while len(path) != moves:
    direction = str(input("Pick a direction \n 'up' 'down' 'left' or 'right'\n"))
    path.append(direction)
for x in range(0,moves):
    if path[cmove] == 'left':
        goleft()
    if path[cmove] == 'right':
        goright()
        savepoint()
        cory, corx = savepoint()
    if path[cmove] == 'up':
        goup()
    if path[cmove] == 'down':
        godown()
    cmove +=1
turtle.penup()
turtle.goto(corx, cory)
turtle.pendown()
turtle.left(45)
turtle.forward(100)