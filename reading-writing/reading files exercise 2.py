f = open("C:\\Users\\19AByrne.ACC\\Desktop\\py\\reading and writing files\\numbers.txt", 'r')
nums = []
for line in f:
    line = line.strip("\n")
    if line.isdigit() == True:
        line=int(line)
        nums.append(line)   
    print(sum(nums))

