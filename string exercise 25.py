#string exercise 25
name = str(input("Enter your first name. "))
lname = int(len(name))
if lname < 5:
    sur = str(input("Enter your surname. "))
    full = (name+sur)
    Full = (full.upper())
    print(Full)
elif lname > 5 or lname == 5:
    lower = (name.lower())
    print(lower)