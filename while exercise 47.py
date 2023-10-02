#while exercise 47
num = int(input("enter a number. "))
num2 = int(input("enter another number. "))
nsum = num + num2
print(nsum)
yn = str(input("Do you want to add another number? "))
while yn == "y":
    varnum = int(input("Enter another number. "))
    nsum = nsum + varnum
    print(nsum)
    yn = str(input("Do you want to add another number? "))
print(nsum)