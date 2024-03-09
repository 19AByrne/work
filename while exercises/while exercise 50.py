#while exercise 50
num = int(input("Enter a number between 10 and 20. "))
while num < 10 or num > 20:
    while num < 10:
        print("Too Low")
        print("Try again")
        num = int(input("Enter a number between 10 and 20. "))
    while num > 20:
        print("Too High")
        print("Try again")
        num = int(input("Enter a number between 10 and 20. "))
print("Thank you")