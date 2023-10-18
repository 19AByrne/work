#string exercise 84
postcode = str(input("Enter your postcode\n"))
postcode = postcode.lower()
nums = '1234567890'
final = str()
for x in range(len(postcode)):
    if not postcode[x] in nums:
        final = final+postcode[x]
final = final[0:2].upper()
print(final)