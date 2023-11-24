f = open("shelley.txt", 'r')
userrange = int(input("Enter the start range of lines: "))
userrange2 = int(input("Enter the end range of lines: "))
linecount=0
for x in f:
    if linecount>=userrange and linecount<=userrange2:
        print(x)
    linecount+=1
        
        