string = str(input("Enter a string: "))

upperc = 0
lowerc = 0
digitc = 0
spacec = 0

for x in string:
    if x == " ":
        spacec += 1
    elif x.isdigit():
        digitc += 1
    elif x.isupper():
        upperc += 1
    elif x.islower():
        lowerc += 1

print(f"Uppercase letters: {upperc}\nLowercase letters: {lowerc}\nDigits: {digitc}\nWhitespace: {spacec}")