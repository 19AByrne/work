#loop exercise 41
name = str(input("enter your name. "))
num1 = int(input("enter a number. "))
if num1 < 10:
    for x in range(num1):
        print(name)
else:
    print("Too high")
