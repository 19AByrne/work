#3rd attempt
#drawing any 2d shape with given directions to python and it will automatically turn it 3d by dragging out all the points at a 45 degree angle
import turtle

cmove = 0
fmove = cmove + 1
path = []
oldpath = []
prefix = "cor"
coorvar1 = "x"
coorvar2 = "y"
suffix = str(cmove)
pfx = "cor"
x1 = "x"
y1 = "y"
print("Draw any 2d shape")
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
def thrdim():
    turtle.pendown()
    turtle.left(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.penup()
def savepointx():
    corx = turtle.xcor()
    return corx
def savepointy():
    cory = turtle.ycor()
    return cory
def checkx():
    if path[cmove] != path[fmove]:
        savepointx()
        return savepointx()
    else:
        return False
def checky():
    if path[cmove] != path[fmove]:
        savepointy()
        return savepointy()
    else:
        return False

while len(path) != moves:
    direction = str(input("Pick a direction \n 'up' 'down' 'left' or 'right'\n"))
    path.append(direction)
    print(path)
for x in range(0, moves):
    if path[cmove] == 'left':
        goleft()
        checkx()
        checky()
        globals()['corl'+suffix] = []
        globals()['corl'+suffix].append(savepointx())
        globals()['corl'+suffix].append(savepointy())
    if path[cmove] == 'right':
        goright()
        checkx()
        checky()
        globals()['corl'+suffix] = []
        globals()['corl'+suffix].append(savepointx())
        globals()['corl'+suffix].append(savepointy())
    if path[cmove] == 'up':
        goup()
        checkx()
        checky()
        globals()['corl'+suffix] = []
        globals()['corl'+suffix].append(savepointx())
        globals()['corl'+suffix].append(savepointy())
    if path[cmove] == 'down':
        godown()
        checkx()
        checky()
        globals()['corl'+suffix] = []
        globals()['corl'+suffix].append(savepointx())
        globals()['corl'+suffix].append(savepointy())
    cmove +=1
    Suffix = int(suffix)
    Suffix +=1
    suffix = str(Suffix)
    

#the corl4 complication
Moves = moves
Moves = str(Moves)
globals()['corl'+Moves] = [0, -100]


print("drawing finished")
print("converting to 3D")


for x in range(0, moves):
    x = str(x)
    turtle.goto(globals()['corl'+x][0], globals()['corl'+x][1])
    thrdim()
cmove = 0
for x in range(0, moves):
    turtle.pendown()
    if path[cmove] == 'left':
        goleft()
    if path[cmove] == 'right':
        goright()
    if path[cmove] == 'up':
        goup()
    if path[cmove] == 'down':
        godown()
    cmove +=1
