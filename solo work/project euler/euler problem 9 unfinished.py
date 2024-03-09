#euler problem 9
"""
a+b+c=1000
a^2+b^2=c^2
"""
triplets = []
def checktriplet(a0,b0,c0):
    if a0**2 + b0**2 == c0**2:
        triplets.append((a0,b0,c0))
        return True
    else:
        return False


def checkspecial(a1,b1,c1):
    if a1+b1+c1 == 1000:
        return True
    else:
        return False

a=0
b=0
c=0
SumOf = 1000
while a+b+c != SumOf:
    while c != 1001:
        while b < c:
            while a < b:
                a+=1
                checktriplet(a,b,c)
                print(a,b,c)
            a=0
            b+=1
        a=0
        b=0
        c+=1
print(triplets)


