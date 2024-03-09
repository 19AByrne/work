#euler problem 3
factors = []
num = 13195
primefactors = []
def listfactors(Y, flist):
    floor = num // Y
    div = num / Y
    if floor == div:
        flist.append(Y)
for x in range(1, num):
    listfactors(x, factors)
factors.append(num)
print("found all factors")


def isprime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

for x in range(0, len(factors)):
    if isprime(factors[x]) == True:
        primefactors.append(factors[x])
print("all factors that are prime have been found")
    
print(primefactors[-1])
    
