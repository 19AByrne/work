#project euler problem 1
nums = []
mul = []
for x in range(1,1000):
    nums.append(x)
for x in range(1,1000):
    if (x // 5) == (x / 5):
        mul.append(x)
    elif (x // 3) == (x / 3):
        mul.append(x)
mult = 0
for x in range(0, len(mul)):
    mult += mul[x]
print(mult)