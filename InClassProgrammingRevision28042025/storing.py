f = open('Data.csv', 'r')
headers = f.readline()
headers = headers.strip('\n')
headerslist = headers.split(',')

dictionary = {}
for index,line in enumerate(f):
    tempdic = {}
    line = line.strip('\n')
    line = line.split(',')
    for i,x in enumerate(line):
        tempdic[ headers[i] ] = x.strip(' ')
    dictionary[index] = tempdic

f.close()

print(dictionary)

f = open('NewData.csv', 'w')
f.write(f'{headers}\n')
for i, v in dictionary.items():
    for h, x in v.items():
        f.write(f'{x}')
        
f.close()


