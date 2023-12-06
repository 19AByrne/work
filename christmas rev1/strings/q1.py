vowels = "aeiou"
vowelcount = 0

string = str(input("Enter a string: "))
string = string.lower()

for x in string:
    if x in vowels:
        vowelcount+=1
        
print(f"Vowels: {vowelcount}")