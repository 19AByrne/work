f = open('names.txt', 'r')
for line in f:
    print(line) 

f = open('names.txt', 'a')
inp = input('enter name: ')
f.write(f', {inp}')
f.close()

f = open('names.txt', 'r')
for line in f:
    print(line) 