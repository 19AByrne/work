#additional function exercises 4
import math

def factorial(num):
    fact = 1
    if num >= 1:
        for x in range(1,num+1):
            fact=fact*x
    return fact

print(factorial(5))