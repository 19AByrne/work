#string exercise 86
password = str(input("Enter a password\n"))
passwordu = password.upper()
passwordnew = str(input("Enter the password again\n"))
passwordnewu = passwordnew.upper()
if passwordu == passwordnewu:
    if password == passwordnew:
        print("cheers")
    else:
        print("They must be in the same case")

    