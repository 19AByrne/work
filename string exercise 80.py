#string exercise 80
name = str(input("Enter your name\n"))
print(f"Your name has {len(name)} characters")
surname = str(input("Enter your surname\n"))
print(f"Your last name has {len(surname)} characters")
full = (name+" "+surname)
print(full)
print(f"Your full name has {len(full)} characters")