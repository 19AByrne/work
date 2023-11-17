#additional function exercises 9
samplist = [1,2,3,4,5,6,7,8,9]
def evennums(l):
    newlist = []
    for x in range(len(l)):
        if not l[x]%2:
            newlist.append(l[x])
        else:
            pass
    return newlist
print(evennums(samplist))