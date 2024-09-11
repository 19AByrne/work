f = open('exercise.csv', 'r')
header = f.readline()

listoflines = []
for line in f:
    line = line.strip('\n')
    line = line.split(',')
    listoflines.append(line)

listoflines = [x for x in listoflines if not x.count('')]

for l in listoflines:
    l = [float(x) for x in l]


print(*listoflines, sep='\n')