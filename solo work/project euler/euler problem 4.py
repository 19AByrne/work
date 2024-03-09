#euler problem 4
num1 = 1
num2 = 1
mul = []
pals = []
while num2 != 1000:
    while num1 != 1000:
        num3 = num1 * num2
        num1 += 1
        mul.append(num3)
    num1 = 0
    num3 = num1 * num2
    num2 += 1
    mul.append(num3)
mul.sort()
mul = list(dict.fromkeys(mul))

def ispal(n):
    n = str(n)
    if len(n) == 6:
        if n[0] == n[-1] and n[1] == n[-2] and n[2] == n[-3]:
            n = int(n)
            return True
#     if len(n) > 2:
#         if n[0] == n[-1] and n[1] == n[-2]:
#             n = int(n)
#             return True
#         else:
#             return False
#     elif len(n) > 3:
#         if n[0] == n[-1] and n[1] == n[-2] and n[2] == n[-3]:
#             n = int(n)
#             return True
#         else:
#             return False
#     elif len(n) > 4:
#         if n[0] == n[-1] and n[1] == n[-2] and n[2] == n[-3] and n[3] == n[-4]:
#             n = int(n)
#             return True
#         else:
#             return False
#     elif len(n) > 5:
#         if n[0] == n[-1] and n[1] == n[-2] and n[2] == n[-3] and n[3] == n[-4] and n[4] == n[-5]:
#             n = int(n)
#             return True
#         else:
#             return False
#             
    
for x in range(0, len(mul)):
#     ispal(mul[x])
    if ispal(mul[x]) == True:
        pals.append(mul[x])
    else:
        pass
print(pals[-1])
print(pals)
        