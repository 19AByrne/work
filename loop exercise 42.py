#loop exercise 42
total = 0
for x in range(0,5):
    num = int(input("Enter a number.\n"))
    yn = str(input("Do you want that number included? "))
    yn = yn.lower()
    if yn == "yes":
        total = total + num
    else:
        pass
print(f"Your total is {total}")