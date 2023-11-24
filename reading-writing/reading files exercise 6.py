filename = str(input("Enter the file you want to open:\n"))
f = open(filename, 'r')
nums = []
for x in f:
    x = x.strip("\n")
    if x.isdigit() == True:
        x=int(x)
        nums.append(x)
total = 0
for i in nums:
    total+=i
mean = total/len(nums)
print(mean)