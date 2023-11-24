f = open('smthn.txt','r')
newline = ''
for x in f:
    newx = x.title()
    newline = newline+' '+newx
newline = newline.strip()    
print(newline)