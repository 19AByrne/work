f=open('linex.txt','r')
for x in f:
    line = x.split()
    if len(line) >=8:
        print(x)