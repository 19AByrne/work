f = open('books.csv', 'r')
header = f.readline()
header = header.strip('\n')
header = header.split(', ')
for l in f:
    print(l, end='')
f.close()

print('\n')
print('How many records do you want to add')
records = int(input())


f = open('books.csv', 'a')
for i in range(records):
    f.write('\n')
    newline = []
    for x in header:
        print(f'Enter value for {x}')
        newline.append(str(input()))
    
    for j,x in enumerate(newline):
        if j != 2:
            f.write(f'{x}, ')
        else:
            f.write(f'{x}')
        
f.close()




f = open('books.csv', 'r')
header = f.readline()
# years = []
# for line in f:
#     line = line.strip('\n')
#     line = line.split(', ')
#     
#     if not line[2] in years:
#         years.append(line[2])
# print(*years)

useryears = int(input('Enter start year: '))
useryeare = int(input('Enter end year  : '))
for line in f:
    line = line.strip('\n')
    line = line.split(', ')
    year = int(line[2])
    if year >= useryears and year <= useryeare:
        print(line[0])
