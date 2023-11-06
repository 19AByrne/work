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
        print("correct")
    else:
        pass
gg = think()    
while gg != comp_num:
    sub(gg)
    gg = think()