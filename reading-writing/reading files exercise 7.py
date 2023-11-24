f = open('shelley.txt', 'r')
charcount = 0
alphanum=('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
for x in f:
    for i in x:
        if not i == " " and not i == "\n":
            charcount+=1
print(charcount)