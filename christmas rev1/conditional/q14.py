n = int(input("Enter a natural number: "))
if n == 0:
    total = 1
elif n < 0:
    print("Factorials don't exist for negative numbers");print("input a NATURAL number")
else:
    total = 1
    for x in range(1,n+1):
        total *=x
try: print(total)
except: NameError
#factorial