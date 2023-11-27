#christmas revision exercise 1 q10
import math
sqrt = math.sqrt
a = int(input("Enter the length of side a for a tri: "))
b = int(input("Enter the length of side b for a tri: "))
c = int(input("Enter the length of side c for a tri: "))
s = (a+b+c)/2
area = sqrt(s*(s-a)*(s-b)*(s-c))
print(f"area is {area}")
