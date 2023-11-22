f = open("C:\\Users\\19AByrne.ACC\\Desktop\\py\\reading and writing files\\shelley.txt", 'r')
linecount = 0
emptylinecount = 0
for line in f:
    if line != "\n":
        linecount+=1
    else:
        emptylinecount+=1
print(f"{linecount} lines\n{emptylinecount} empty lines")


