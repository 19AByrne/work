f = open("C:\\Users\\19AByrne.ACC\\Desktop\\py\\reading and writing files\\shelley.txt", 'r')
linecount = 0
for line in f:
    if line != "\n":
        linecount+=1
print(linecount)

