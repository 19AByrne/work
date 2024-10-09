def sumoflist(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + sumoflist(l[1:])
    
print(sumoflist([1,2,3]))