words = ['apple','banana','cherry']
def firstletter(x):
    return x[0]

newlist = list(map(firstletter, words))
print(newlist)