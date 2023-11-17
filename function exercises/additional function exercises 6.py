#additional function exercises 6
def casecount(s):
    Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    Uppercount = 0
    Lowercount = 0
    for x in range(len(s)):
        if s[x] in Alpha:
            Uppercount+=1
        elif s[x] in alpha:
            Lowercount+=1
    return Uppercount, Lowercount

casecount = casecount('The quick Brow Fox')
print(f"No. of Upper case characters: {casecount[0]}")
print(f"No. of lower case characters: {casecount[1]}")