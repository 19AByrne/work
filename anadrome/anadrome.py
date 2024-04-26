f = open('words.txt','r')
    
def ac(w1,w2):
    if w1[::-1] == w2:
        return True
    else:
        return False

words = [word.strip('\n') for word in f if len(word) > 6]
anadromes = []

def p(w):
    return w[::-1]

for word in words:
    if p(word) in words and p(word) != word:
        print(word,'and',p(word))
        words.remove(p(word))
        words.remove(word)
        