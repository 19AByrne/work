#caesar cipher
Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
key = int(input("Enter a key.\n"))
for x in range(0, key):
    pop = alphabet.pop(0)
    alphabet.append(pop)
inp = str(input("Enter any phrase.\n"))
inp = inp.lower()
count = 0
for x in inp:
    if inp[count] in Alphabet:
        inp = inp.replace(inp[count], alphabet[Alphabet.index(inp[count])])
    else:
        pass
    count +=1
print(inp)