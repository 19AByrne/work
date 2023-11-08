#function exercise 119
import random
r = random
def function():
    num1 = int(input("Enter a low number: "))
    num2 = int(input("Enter a high number: "))
    return r.randint(num1,num2)
comp_num = function()
print(comp_num)

def think():
    print("I am thinking of a number...")
    return int(input("Guess what number i'm thinking of: "))
    
def sub(guess):
    if guess == comp_num:
        return ("correct")
    else:
        return ("incorrect")
gg = think()    
while gg != comp_num:
    print(sub(gg))
    gg = think()
print(sub(gg))