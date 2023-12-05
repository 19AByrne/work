n = int(input("Enter a number: "))
e = int(input("Enter an exponent: "))
total = 1
if e > 0:
    for x in range(e):
        total *= n
    print(total)
elif e < 0:
    e = abs(e)
    for x in range(e):
        total *= n
    total = (1/total)
    print(total)
else:
    print(total)
        
#exponents