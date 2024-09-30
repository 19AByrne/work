f = open('ajb.txt', 'r')
table = {}
length = 0
for line in f:
    line = line.strip('\n')
    line = line.split(' ')
    print(line)
    if line != []:
        lengthbuffer = len(max(line, key = len))
        if length < lengthbuffer:
            length = len(max(line, key = len))
    for i in line:
        i = i.strip('-.,\'')
        count = 0
        for ii in line:
            ii = ii.strip('-.,\'')
            if i == ii:
                count += 1
            table[i] = count    
print(table)   

print('\033[4mword'+(' ')*(length)+'count\033[0m')
for x in table:
    if table[x] > 0:
        print(f'{x}'+(' ')*(length-len(x)+1)+'|'+(' ')*(4)+f'{table[x]}')