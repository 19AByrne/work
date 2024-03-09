import random
import turtle
import time
t=turtle
r=random
t.hideturtle()
t.speed(10)
t.bgcolor('black')
t.color('white')
# nodes = 5
# edges = 10
nodes = int(input("How many nodes does your graph have:\n"))
edges = int(input("How many edges does your graph have:\n"))
ps = {}
pskey = []
adj = {}
adjkey = []
alpha = 'abcdefghijklmnopqrstvwuxyz'
t.penup()
    
for x in range(nodes):
    ps.update({alpha[x]:t.pos()})
    pskey.append(alpha[x])
    t.dot(5)
    t.forward(100)
    t.left(360/nodes)
done = []

#labelling points
t.right(360/nodes)
t.backward(100)
for p in pskey:
    t.forward(120)
    t.write(p)
    t.backward(20)
    t.left(360/nodes)
    
    
for x in range(nodes):
#     print(f"{x} x")
    for i in range(nodes):
#         print(f"{i} i")
        selectededge = (pskey[x]+pskey[i])
        if selectededge[0] in done or selectededge[1] in done:
            pass
        else:
            inpadj = int(input(f"What is the adjacency of edge {selectededge}\n"))
            if inpadj >= 1:
                adj.update({selectededge:inpadj})
                adjkey.append(selectededge)
            else:
                pass
    done.append(alpha[x])


    
for x in range(len(adjkey)):
    selectededge = adjkey[x]
    if adj[selectededge] == 1:
        t.penup()
        t.goto(ps[selectededge[0]])
        t.pendown()
        t.goto(ps[selectededge[1]])

print(adj)
print(adjkey)


weight = {}
weightkey = []
for x in range(len(adj)):
    selectededge = adjkey[x]
    flippedselectededge = selectededge[::-1]
    inpweight = int(input(f"What is the weight of edge {selectededge}\n"))
    weight.update({selectededge:inpweight})
    weightkey.append(selectededge)
    weight.update({flippedselectededge:inpweight})
    weightkey.append(flippedselectededge)

weightcopy = weight.copy()

selectedpoints = ['a']
MSTedges = []
while not len(MSTedges)+1 == nodes: #MST prims loop

    for point in selectedpoints: #checking if it ends in a
        for y in weightkey:
            if point == y[0]:
                weightkey.remove(y) #removing anything from the key list
                del weight[y] #removing anything from the real dict

    #finding the lowest weight in selected edges
    tempweights = []
    for point in selectedpoints:
        for edge in weightkey:
            if point == edge[1]:
                tempweights.append(weight[edge])            
    tempweightforedge = min(tempweights)
    edgeoflowestweight = (list(weight.keys())[list(weight.values()).index(tempweightforedge)]) #stolen off stackoverflow

    MSTedges.append(edgeoflowestweight)
    selectedpoints.append(edgeoflowestweight[0])
    
print(MSTedges)

#drawing mst
t.forward(100);t.left(360/nodes) #readjusting cursor
t.color('green')
for edge in MSTedges:
    t.penup()
    t.goto(ps[edge[0]])
    t.dot(7)
    t.pendown()
    t.goto(ps[edge[1]])
    t.dot(7)
    
#getting the MST weight
print(weightcopy)
MSTedges_n = []
for edge in MSTedges:
    MSTedges_n.append(weightcopy[edge])
MSTweight = sum(MSTedges_n)

#displayinf MST weight
t.penup()
t.goto(ps['a'])
t.right(90)
t.forward(50)
t.write(f"MST weight - {MSTweight}", False, align="left", font=('Arial', 12))
    
t.done()