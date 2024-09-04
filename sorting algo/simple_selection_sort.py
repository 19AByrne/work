def simple_selection(L):
    for m in range(len(L)):
        smalli = m
        for i in range(m+1,len(L)):
            if L[smalli] > L[i]:
                smalli = i
        L[m], L[smalli] = L[smalli], L[m]
    return L

print(simple_selection([9,2,3,7,5]))
