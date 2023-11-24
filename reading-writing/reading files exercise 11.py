f = open('badSpelling.txt','r')
nums = ('0123456789')
words = []
for x in f:
    line =x.split()
    for i in line:
        if i[-1] in nums:
            words.append(i)
            
print(words)