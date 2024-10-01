f = open('names.txt', 'r')
for l in f:
    print(l)
    list = l.split(', ')
print('''Type in existing name''')
inp = str(input())
if inp in l:
    list.remove(inp)
f.close()

f = open('names2.txt', 'w')
f.write(str(list))
f.close()
