f = open('exercise.csv', 'r')
d = open('durations.txt', 'r')
header = f.readline()

listoflines = []
for line in f:
    line = line.strip('\n')
    line = line.split(',')
    listoflines.append(line)

listoflines = [x for x in listoflines if not x.count('')]

for l in listoflines:
    for i in range(len(l)):
        l[i] = float(l[i])

# print(*listoflines, sep='\n')

durations = []
for k in d:
    k = k.strip('\n')
    durations.append(int(k))

averages = []
for t in durations:
    total = 0
    count = 0
    for line in listoflines:
        if t == line[0]:
           count += 1
           total += line[3]
    averages.append((total/count))

print('Session duration(m) , Average calories burned')
for i in range(len(durations)):
    print(f'{durations[i]}                    {averages[i]}')             
print('done')