def tento13(ISBN):
    use1 = True
    ISBN = (ISBN[:-1]).strip('-')
    ISBN = '978-'+ISBN
    ISBNsave = ISBN
    for x in ISBN:
        if x == '-':
            i = ISBN.find(x)
            ISBN = ISBN[:i]+ISBN[i+1:]
    ISBN = [int(x) for x in ISBN]
    for i,x in enumerate(ISBN):
        if use1 == True:
            ISBN[i] = x*1
            use1 = False
        else:
            ISBN[i] = x*3
            use1 = True 
    ISBN = sum(ISBN)
    check = ISBN % 10
    if check == 0:
        check = 0
    else:
        check = 10-check
    ISBN = ISBNsave+'-'+str(check)
    return ISBN

print(tento13('1-85326-158-0'))





