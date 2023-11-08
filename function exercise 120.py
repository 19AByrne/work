#function exercise 120
import random
r=random
selection = int(input("1) Addition\n2) Subtraction\nEnter 1 or 2: "))
def add():
    n1 = r.randint(5,20)
    n2 = r.randint(5,20)
    s = n1+n2
    g = int(input(f"What is {n1} + {n2}?\n"))
    return s,g
    
def sub():
    n1 = r.randint(25,50)
    n2 = r.randint(1,25)
    d = n1 - n2
    g = int(input(f"What is {n1} - {n2}?\n"))
    return d,g
    
def check(func):
    nums = (func())
    if nums[0] == nums[1]:
        return True
    else:
        return False
       
if selection == 1:
    print(check(add))
elif selection == 2:
    print(check(sub))
    