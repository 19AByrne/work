#euler problem 2
fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
fibe = []
fibet = 0

def new():
    new = fib[-1] + fib[-2]
    fib.append(new)
    
while fib[-1] < 4000000:
    new()
if fib[-1] > 4000000:
    fib.remove(fib[-1])
for x in range(0, len(fib)):
    fib[x] = str(fib[x])
    if (fib[x])[-1] == '2' or (fib[x])[-1] == '4' or (fib[x])[-1] == '6' or (fib[x])[-1] == '8' or (fib[x])[-1] == '0':
        fibe.append(fib[x])
for x in range(0, len(fibe)):
    fibe[x] = int(fibe[x])
    fibet += fibe[x]
print(fibet)