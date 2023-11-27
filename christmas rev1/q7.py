#christmas revision exercise 1 q7
a = str(input("Enter a number: "))
b = str(input("Enter another number: "))
print(f"a is {a}")
print(f"b is {b}")
print("---SWAPPING---")
a=a+'-'+b
b=a[:a.find('-')]
a=a[a.find('-')+1:]
print(f"a is {a}")
print(f"b is {b}")
