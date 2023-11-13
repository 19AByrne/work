#string exercise 87
word = str(input("Type in a word\n"))
word = word[::-1]
print(*word, sep='\n')