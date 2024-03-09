def pc(x):
    if x == x[::-1]:return True
    else: return False
userstring = str(input("Enter any string: "))
if pc(userstring) == True: print(f"{userstring} is a palindrome")
else: print(f"{userstring} is not a palindrome")