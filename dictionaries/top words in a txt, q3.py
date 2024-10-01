#ITS SLIGHTLY WRONG BUT IDC 

f = open('book.txt', 'r')
table = {}
length = 0

for line in f:
    line = line.strip('\n')
    line = line.split(' ')
    if line != []:
        lengthbuffer = len(max(line, key = len))
        if length < lengthbuffer:
            length = len(max(line, key = len))
    
    for x in line:
        x = x.strip('.,-\'')
        line = list(dict.fromkeys(line))
        if not x in table:
            table[x] = line.count(x)
        else:
            table[x] = table[x] + line.count(x)

def sort_dict(d):
    sorted_list = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_list)

table = sort_dict(table)



        
print('top10')       
print('\033[4mword'+(' ')*(length)+'count\033[0m')
for i,x in enumerate(table):
    if i < 11:
        print(f'{x}'+(' ')*(length-len(x)+1)+'|'+(' ')*(4)+f'{table[x]}')