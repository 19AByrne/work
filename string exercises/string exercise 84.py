#string exercise 84#
postcode = str(input("Enter your postcode\n"))
postcode = postcode.lower()
nums = '1234567890'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
final = str()
letterCount = 0
for x in range(len(postcode)):
    selectedchar = postcode[x]
    if selectedchar in nums:
        final = final+selectedchar
    elif selectedchar in alpha:
        if letterCount < 2:
            selectedchar = selectedchar.upper()
            final = final+selectedchar
        else:
            selectedchar = selectedchar.lower()
            final = final+selectedchar
        letterCount += 1
print(final)
