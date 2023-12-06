string = str(input("Enter a string: "))
reversestring = string[::-1]
if string == reversestring:
    print("This string is a palindrome")
else:
    print("This string is not a palindrome")
