f = open('courses.csv','r')

count = 0
for line in f:
    line = line[:-1]
    fields = line.split(',')
    if fields[0]=='CS':
        print(fields[0],fields[1])
        count += 1
        
f.close()