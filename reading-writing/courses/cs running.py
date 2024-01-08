f = open('results.txt','r')
ULcount = 0
DCUcount = 0
TCDcount = 0
schoolcount = 0
schools = []
for line in f:
    line = line.strip('\n')
    field = line.split(',')
    if not field[1] in schools:
        schoolcount+=1
        schools.append(field[1])
    if field[1] == 'UL':
        ULcount += 1
    elif field[1] == 'DCU':
        DCUcount += 1
    elif field[1] == 'TCD':
        TCDcount += 1

print(f"There are {schoolcount} schools in all.")
print(f"UL has {ULcount} result(s)")
print(f"DCU has {DCUcount} result(s)")
print(f"TCD has {TCDcount} result(s)")