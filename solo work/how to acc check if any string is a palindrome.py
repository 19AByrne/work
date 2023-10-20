string = str(input("Enter any string\n"))
reversestring = string[::-1]
if reversestring == string:
    print("palindrome")
else:
    print("no")