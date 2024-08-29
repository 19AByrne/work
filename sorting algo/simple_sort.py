def simple(L):
    e = []
    for x in range(len(L)):
        si = 0
        for i in range(len(L)):
            if L[i] < L[si]:
                si = i
        e.append(L[si])
        L.remove(L[si])
    return e
List = [9,2,3,7,5]
print(simple(List))
            
        