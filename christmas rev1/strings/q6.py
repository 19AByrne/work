name = str(input("Enter your full name\n"))
initials = name[0].upper()+"."
for x in range(len(name)):
    if name[x] == " ":
        initials = initials+name[x+1].upper()+"."
print(initials)
