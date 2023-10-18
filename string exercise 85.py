#string exercise 85
name = str(input("Enter your name\n"))
vowels = 'aeiou'
vowelcount = 0
for x in range(len(name)):
    if name[x] in vowels:
        vowelcount += 1
    else:
        pass
print(vowelcount)