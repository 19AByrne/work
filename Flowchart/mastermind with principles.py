import random
import os
import time
from colorama import Fore, Back, Style
colours = ['g','c','m','o','p','b']
comp = []
tries = 1

title =f"""
                     _                      _           _ 
 _ __ ___   __ _ ___| |_ ___ _ __ _ __ ___ (_)_ __   __| |
| '_ ` _ \ / _` / __| __/ _ \ '__| '_ ` _ \| | '_ \ / _` |
| | | | | | (_| \__ \ ||  __/ |  | | | | | | | | | | (_| |
|_| |_| |_|\__,_|___/\__\___|_|  |_| |_| |_|_|_| |_|\__,_|
                                                          
                               _           
  _ __ _ _ ___ ______  ___ _ _| |_ ___ _ _ 
 | '_ \ '_/ -_|_-<_-< / -_) ' \  _/ -_) '_|
 | .__/_| \___/__/__/ \___|_||_\__\___|_|  
 |_|                                         """



print(title)
input()
print('\n' * 100)

rules = f"""
           _        
  _ _ _  _| |___ ___
 | '_| || | / -_|_-<
 |_|  \_,_|_\___/__/
                    
• There are six possible colours:
    {Fore.GREEN}(g)reen{Fore.WHITE}, {Fore.LIGHTCYAN_EX}(c)yan{Fore.WHITE}, {Fore.LIGHTMAGENTA_EX}(m)agenta{Fore.WHITE}, {Fore.YELLOW}(o)range{Fore.WHITE}, {Fore.MAGENTA}(p)urple{Fore.WHITE}, {Fore.WHITE}(b)lack{Fore.WHITE}
    
• The computer will generate a list of 4 colours, (they can be repeated).

• You will guess the order of colours, the computer will return how many were
    in the right position and how many were not.
    
• You will have infinite tries.

press enter to continue"""
print(rules)
input()
print('\n' * 100)

if len(comp) == 4:
    print(colours)
else:
    for i in range(4):
        x = random.choice(colours)
        comp.append(x)
while True:
    user = input(f'Enter guess below\n')
    user = user.split()
    user = [x.lower() for x in user]
    
    
    #tolerance for error
    setcomplete = False
    while len(user) != 4:
        print(f'You have {Fore.LIGHTRED_EX}not{Fore.WHITE} entered 4 colours, please try again')
        user = input(f'Enter guess below\n')
        user = user.split()
        user = [x.lower() for x in user]
        print(user)
    for c in user:
        if c in colours:
            setcomplete = True
        else:
            setcomplete = False
            break
    while not setcomplete:
        for i,colour in enumerate(user):
            if not colour in colours:
                print(f'{colour} is not in our chosen colours')
                print(f'please enter a new value for position {i+1}')
                user[i] = input()
                while not user[i] in colours:
                    print('TRY AGAIN')
                    user[i] = input()
        setcomplete = True

    correct = 0
    off = 0
    for x in range(len(user)):
        if user[x] == comp[x]:
           correct += 1
        elif user[x] in comp:
           off += 1
    print(f'\nCorrect colour in correct place: {correct}')
    print(f'Correct colour in wrong place {off}\n')
    if correct == 4:
        print(f'Well done it took you {tries} tries')
        break
    else:
        tries += 1
