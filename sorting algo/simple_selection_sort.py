def simple_selection(L):
    mark = 0
    for i in range(len(L)):
        for x in range(len(L)-1):
            s = 0
            for i in range(len(L)):
                if L[i] < L[s]:
                    s = i
        buffer = L[mark]
        L[mark] = L[s]
        L[s] = buffer
            
    return L            
print(simple_selection([7,6,5,4,3,2,1]))