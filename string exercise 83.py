#string exercise 83
word = str(input("TYPE A WORD IN UPPER CASE\n"))
uword = word.upper()
lword = word.lower()
while word != uword:
    print("THATS NOT UPPER CASE TRY AGAIN")
    word = str(input("TYPE A WORD IN UPPER CASE\n"))
print("cheers")
