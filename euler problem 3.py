#euler problem 3
factors = []
num = 13195
primefactors = [1, num]
def listfactors(Y, flist):
    floor = num // Y
    div = num / Y
    if floor == div:
        flist.append(Y)
for x in range(1, num):
    listfactors(x, factors)
factors.append(num)
print(factors)

def checkprime(Y):
    floor = num // Y
    div = num / Y
    for x in range(1, len(factors)):
        if floor == [primefactors] and div == [primefactors]:
            primefactors.append(x)
        
        
print(primefactors)
    