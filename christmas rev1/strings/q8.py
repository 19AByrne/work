string = str(input("Enter a string: "))
for x in range(len(string)+1):
    print(string[x:]+string[:x])