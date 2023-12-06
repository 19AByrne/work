def validate(pw):
    uppercount = 0; lowercount = 0; digitcount = 0
    for x in pw:
        if x.isupper():   uppercount += 1
        elif x.islower(): lowercount += 1
        elif x.isdigit(): digitcount += 1
    if not uppercount >= 1 or not lowercount >= 1 or not digitcount >= 1 or not len(pw) >= 8:
        return False
    else:
        return True 
PASSWORD = str(input("Enter Password: "))
if validate(PASSWORD): print("Valid")
else: print("invalid password")
            