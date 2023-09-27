#loop exercise 43
count = 1
updwn = str(input("Do you want to count up or down? "))
updwn = updwn.lower()
if updwn == "up":
    num = int(input("Enter a top number. "))
    while count != num:
        print(count)
        count = count + 1
        
    print(num)
elif updwn == "down":
    num = int(input("Enter a number below 20"))
    count = 20
    print(count)
    while count != num:
        count = count - 1
        print(count)
else:
    print("I don't understand.")
        
        
    
