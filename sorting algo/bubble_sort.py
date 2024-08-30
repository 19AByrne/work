List = [4,3,2,1]
def bubble(L):
    for p in range(len(L)-1):
        for b in range(len(L)-1):
            if L[b] > L[b+1]:
                buffer = L[b]
                L[b] = L[b+1]
                L[b+1] = buffer
    return(L)      
print(bubble(List))
