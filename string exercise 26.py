#string exercise 26
eng = str(input("Enter any word. "))

def vowel():
    word = (eng)
    endword = ("way")
    newword = (word+endword)
    return newword
    
def constanant():
    letter = (eng[0])
    word = (eng.strip(eng[0]))
    endword = ("ay")
    newword = (word+letter+endword)
    return newword
    
if eng[0] == "a" or eng[0] == "A" or eng[0] == "e" or eng[0] == "E" or eng[0] == "i" or eng[0] == "I" or eng[0] == "o" or eng[0] == "O" or eng[0] == "u" or eng[0] == "U":
    vowel()
    print(vowel())
else:
    constanant()
    print(constanant())
    
