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
    
    
all45 = []
for line in listoflines:
    if line[0] == 45:
        all45.append(line)


def last(l):
    return l[-1]
all45 = sorted(all45, key=last, reverse=1)
top45 = all45[:20]
bot45 = all45[-20:]

print('\n')
print('average of top 20 exercise of length 45 minutes')
total = 0
for v in top45:
    total += v[-1]
#     print(v[-1])
print(total/len(top45))

total = 0
for v in bot45:
    total += v[-1]
#     print(v[-1])
print('average of bottom 20 exercise of length 45 minutes')
print(total/len(bot45))


print('\n')
all60 = []
for line in listoflines:
    if line[0] == 60:
        all60.append(line)

all60 = sorted(all60, key=last, reverse=1)
top60 = all60[:20]
bot60 = all60[-20:]

print('average of top 20 exercise of length 60 minutes')
total = 0
for v in top60:
    total += v[-1]
#     print(v[-1])
print(total/len(top60))

print('average of bottom 20 exercise of length 60 minutes')
total = 0
for v in bot60:
    total += v[-1]
#     print(v[-1])
print(total/len(bot60))

print('\n')
print('possible exercise duration types')
print(*durations, sep=', ', end='\n\n')
userduration = int(input('Enter duration for your exercise: \n'))
while not userduration in durations:
    userduration = int(input('invalid input, try again: \n'))
usercalories = float(input('Enter the number of calories you burnt: \n'))

print(f'''You burnt {usercalories} in {userduration} minutes.
the average number of calories burnt in that time: {averages[durations.index(userduration)]}
''')
    
