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
authors = []
for line in f:
    line = line.split(', ')
    if not line[1] in authors:
        authors.append(line[1])

f.close()

print('Enter an author')
userauthor = str(input())
while not userauthor in authors:
    print('invalid author')
    userauthor = str(input())

f = open('books.csv', 'r')
for line in f:
    line = line.strip('\n')
    line = line.split(', ')
    if line[1] == userauthor:
        print(line[0])
        
f.close()
