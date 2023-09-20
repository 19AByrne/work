#string exercise 21
name = str(input("Enter your first name. "))
lname = str(input("Enter your surname. "))
full = (name,lname)
fulllen = len(name)+len(lname)
print("Your full name is", *full,"and it has",fulllen,"letters in it.")