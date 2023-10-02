#while exercise 49
compnum = 50
num = int(input("Enter a number. "))
count = 0
while num != compnum:
    if num > compnum:
        print("Too High")
    if num < compnum:
        print("Too Low")
    num = int(input("Enter another number. "))
    count +=1
print(f"Well done, you took {count} attempts.")