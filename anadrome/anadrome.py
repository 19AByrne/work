import itertools
f = open('words.txt','r')
    
def ac(w1,w2):
    if w1[::-1] == w2:
        return True
    else:
        return False

words = [word.strip('\n') for word in f if len(word) > 6]

for x, y in itertools.combinations(words, 2):
    if ac(x,y) == True:
        print(x,y)