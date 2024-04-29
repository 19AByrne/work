import random
colours = ['green','blue','pink','orange','purple','black']
comp = []
tries = 1
if len(comp) == 4:
    print(colours)
else:
    for i in range(4):
        x = random.choice(colours)
        comp.append(x)

while True:
    user=input(f'4 colours from {colours} with spaces between each\n')
    user = user.split()
    correct = 0
    off = 0
    for x in range(len(user)):
        if user[x] == comp[x]:
           correct += 1
        elif user[x] in comp:
           off += 1
    print(f'Correct colour in correct place: {correct}')
    print(f'Correct colour in wrong place {off}')
    if correct == 4:
        print(f'Well done it took you {tries} tries')
        break
    else:
        tries += 1