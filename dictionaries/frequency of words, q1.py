inp = str(input('Enter a sentence\n'))
inp = inp.split()
inp = [x.lower() for x in inp]
length = len(max(inp, key = len))
print(length)

table = {}
for i in inp:
    count = 0
    for ii in inp:
        if i == ii:
            count += 1
        table[i] = count
       
print('\033[4mword'+(' ')*(length)+'count\033[0m')
for x in table:
    print(f'{x}'+(' ')*(length-len(x)+1)+'|'+(' ')*(4)+f'{table[x]}')

