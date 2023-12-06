string = str(input("Enter a string: "))
newstring = ""
for x in range(len(string)):
    newstring = newstring+string[-(x+1)]
print(newstring)