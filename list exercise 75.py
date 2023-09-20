#list exercise 75
lst = [222, 333, 444]
print("the first number in the list is", lst[0])
print("The second number in the list is", lst[1])
print("the last number in the list is", lst[-1])
usnum = int(input("Enter a three digit number. "))
if usnum in lst:
    print("That number is in the list")
else:
    print("That number is not in the list")