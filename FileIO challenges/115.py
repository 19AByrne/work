f = open('books.csv', 'r')
header = f.readline()
header = header.strip('\n')
print(' ',header)
header = header.split(', ')
for i,l in enumerate(f):
    print(i+1,l, end='')
f.close()
