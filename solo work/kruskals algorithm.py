import random
import turtle
t=turtle
r=random
t.speed(10)

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
      
done = []
weight = {}
weightkey = []
for x in range(len(adj)):
    selectededge = adjkey[x]
    inpweight = int(input(f"What is the weight of edge {selectededge}\n"))
    weight.update({selectededge:inpweight})
    weightkey.append(selectededge)
    done.append(alpha[x])
print(weight)
print(weightkey)


t.done()
