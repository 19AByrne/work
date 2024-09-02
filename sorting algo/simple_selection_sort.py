def simple_selection(L):
    for m in range(len(L)):
        for i in range(m+1,len(L)):
            if L[i] < L[m]:
                sml = i
        
    print(L[sml])
    return L,i

print(simple_selection([9,2,3,7,5]))