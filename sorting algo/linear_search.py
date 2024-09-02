def Linear_search(L,t):
    for i in range(len(L)):
        if L[i] == t:
            return i
        
print(Linear_search([1,2,3,4,5,6,5,6,5],5))