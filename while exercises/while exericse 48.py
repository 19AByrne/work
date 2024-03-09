#while exercise 48
name = str(input("Enter a name of somebody you want to invite to the party. "))
count = 0
print(f"{name} has now been invited")
count =+1
yn = str(input("Do you want to invited anyone else? "))
while yn == "yes":
    name = str(input("Enter a name of somebody you want to invite to the party. "))
    print(f"{name} has now been invited")
    count =+1
    yn = str(input("Do you want to invited anyone else? "))
print(f"There are {count} people invited")
