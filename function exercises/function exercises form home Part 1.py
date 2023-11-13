import random
r = random
def program1():
    print("This program will take user input and tell you the greatest number")
    A = int(input("Enter a number: "))
    B = int(input("Enter a number: "))
    C = int(input("Enter a number: "))
    if A > B and A > C:
        print(f"{A} is the greatest number")
    elif B > A and B > C:
        print(f"{B} is the greatest number")
    elif C > A and C > B:
        print(f"{C} is the greatest number")
# program1()

def program2():
    print("This program will take user input and tell you the greatest number")
    A = int(input("Enter a number: "))
    B = int(input("Enter a number: "))
    C = int(input("Enter a number: "))
    if A > B:
        if A > C:
            print(f"{A} is the greatest number")
        else:
            print(f"{C} is the greatest number")
    else:
        if B > C:
            print(f"{B} is the greatest number")
        else:
            print(f"{C} is the greatest number")
# program2()

def program3():
    print("This program will take user input and tell you the greatest number")
    A = int(input("Enter a number: "))
    B = int(input("Enter a number: "))
    C = int(input("Enter a number: "))
    maximum = A
    if maximum < B:
        maximum = B
    if maximum < C:
        maximum = C
    print(f"{maximum} is the greatest number")
program3()
