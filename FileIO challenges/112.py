f = open('books.csv')
header = f.readline()

print(header)
for line in f:
    print(line.strip('\n'))

header = header.strip('\n')
header = header.split(', ')

print()
newline = []
for x in header:
    print(f'Enter value for {x}')
    newline.append(str(input()))

print(newline)
f.close()
f = open('books.csv', 'a')

f.write('\n')
for i,x in enumerate(newline):
    if i != 2:
        f.write(f'{x}, ')
    else:
        f.write(f'{x}')
    
f.close()