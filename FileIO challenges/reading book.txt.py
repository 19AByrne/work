f = open('book.txt','r')

frequencyCounter = {}
for line in f:
    line.strip('/n')
    line = line.split(' ')
    for x in line: