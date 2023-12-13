"""
                     _         _                      _             _ 
                    (_)       | |                    (_)           | |
  _ __ _   _ _ __    _ _ __   | |_ ___ _ __ _ __ ___  _ _ __   __ _| |
 | '__| | | | '_ \  | | '_ \  | __/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
 | |  | |_| | | | | | | | | | | ||  __/ |  | | | | | | | | | | (_| | |
 |_|   \__,_|_| |_| |_|_| |_|  \__\___|_|  |_| |_| |_|_|_| |_|\__,_|_|
"""



##hangman
import random
import os
import time
r=random
f = open('words.txt', 'r')
words = []
for word in f:
    word = word.strip("\n")
    if word.isalpha():
        words.append(word)

                  
#
def graphic(cl):
    if cl == 10:
        shellgraphic = """

                   
                   
                   
                   
                   
                    
                  ==="""
    elif cl == 9:
        shellgraphic = """

                   |
                   |
                   |
                   |
                   |
                   |
                  ==="""
    elif cl == 8:
        shellgraphic = """
--------------------
                   |
                   |
                   |
                   |
                   |
                   |
                  ==="""
    elif cl == 7:
        shellgraphic = """
--------------------
        |          |
                   |
                   |
                   |
                   |
                   |
                  ==="""
    elif cl == 6:
        shellgraphic = """
--------------------
        |          |
        O          |
                   |
                   |
                   |
                   |
                  ==="""
    elif cl == 5:
        shellgraphic = """
--------------------
        |          |
        O          |
        |          |
                   |
                   |
                   |
                  ==="""
    elif cl == 4:
        shellgraphic = """
--------------------
        |          |
        O          |
        |\         |
                   |
                   |
                   |
                  ==="""
    elif cl == 3:
        shellgraphic ="""
--------------------
        |          |
        O          |
       /|\         |
                   |
                   |
                   |
                  ==="""
    elif cl == 2:
        shellgraphic = """
--------------------
        |          |
        O          |
       /|\         |
        |          |
                   |
                   |
                  ==="""
    elif cl == 1:
        shellgraphic = """
--------------------
        |          |
        O          |
       /|\         |
        |          |
       /           |
                   |
                  ==="""
    elif cl == 0:
        shellgraphic = """
--------------------
        |          |
        O          |
       /|\         |
        |          |
       / \         |
                   |
                  ==="""
    return shellgraphic
new_words = []
print("""
       ▄█    █▄       ▄████████ ███▄▄▄▄      ▄██████▄    ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄   
      ███    ███     ███    ███ ███▀▀▀██▄   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄ 
      ███    ███     ███    ███ ███   ███   ███    █▀  ███   ███   ███   ███    ███ ███   ███ 
     ▄███▄▄▄▄███▄▄   ███    ███ ███   ███  ▄███        ███   ███   ███   ███    ███ ███   ███ 
    ▀▀███▀▀▀▀███▀  ▀███████████ ███   ███ ▀▀███ ████▄  ███   ███   ███ ▀███████████ ███   ███ 
      ███    ███     ███    ███ ███   ███   ███    ███ ███   ███   ███   ███    ███ ███   ███ 
      ███    ███     ███    ███ ███   ███   ███    ███ ███   ███   ███   ███    ███ ███   ███ 
      ███    █▀      ███    █▀   ▀█   █▀    ████████▀   ▀█   ███   █▀    ███    █▀   ▀█   █▀  
                                                                                         
                                                                                                                                                                                                  
                                         /                        /                   /              /   
 ___  ___  ___  ___  ___       ___  ___ (___       ___  ___      (___  ___       ___ (___  ___  ___ (___ 
|   )|   )|___)|___ |___      |   )|___)|    |   )|   )|   )     |    |   )     |___ |    |   )|   )|    
|__/ |    |__   __/  __/      |    |__  |__  |__/ |    |  /      |__  |__/       __/ |__  |__/||    |__  
|                                                                                                       """)
input(" ")
os.system('cls')
name = str(input("Enter your name: "))
print("Choose Difficulty")
mode = int(input("(1) Easy, (2) Medium, (3) Hard, (4) Impossible\n"))
if mode == 1:
    for word in words:
        if len(word) <= 4:
            word = word.lower()
            new_words.append(word)
elif mode == 2:
    for word in words:
        if len(word) >= 4 and len(word) <= 7:
            word = word.lower()
            new_words.append(word)
elif mode == 3:
    for word in words:
        if len(word) >=7 and len(word) <= 12:
            word = word.lower()
            new_words.append(word)
elif mode == 4:
    for word in words:
        if len(word) > 12:
            word = word.lower()
            new_words.append(word)
os.system('cls')    
difficulty = {1:'Easy',
              2:'Medium',
              3:'Hard',
              4:'Impossible'}
score = 0
chancesleft = 10
guesses = []
# possiblewords = ['ball','apple','keyboard','bench','book','poster']
correctword = r.choice(new_words)
correctword = list(correctword)
word = []
#
# print(*correctword, sep="")
#
game_active = True
def setup():
    global correctword, word, chancesleft, score, guesses, game_active, finalword, recentguess
    game_active = True
    score = 0
    chancesleft = 10
    guesses = []
    correctword = r.choice(new_words)
    correctword = list(correctword)
    recentguess = ""
    word = []
    for x in range(len(correctword)):
        word.append('_')
    finalword = ''
    for x in correctword:
        if x.isalpha():
            finalword = finalword + x
    os.system('cls')
    print(f"Name: {name}")
    print(f"Difficulty: {difficulty[mode]}")
    print(f"Score: {score}")
    print(f"Chances left: {chancesleft}")
    print(f"Guessed letters", guesses)
    print(graphic(chancesleft))
    print(recentguess)
setup()



while game_active:
    if word == correctword:
        print(f"The word was '{finalword}'")
        play_again = str(input("Would you like to play again? y/n\n"))
        if play_again == 'y':
            setup()
        elif play_again == 'n':
            game_active = False
    if chancesleft==0:
        print(f"The word was '{finalword}'")
        play_again = str(input("Would you like to play again? y/n\n"))
        if play_again == 'y':
            setup()
        elif play_again == 'n':
            game_active = False
    print(*word)
    guess = str(input("Guess a letter\n"))
    while len(guess) != 1 and guess.isalpha() == True:
        guess = str(input("Invalid input, please guess again\n"))
    if len(guess) == 1 and guess.isalpha() == True and not guess in correctword and not guess in guesses:
        guesses.append(guess)
    os.system('cls')
    if guess in correctword and not guess in guesses and not guess in word:
        for x in range(len(correctword)):
            if guess == correctword[x]:
                word[x] = guess
        recentguess="correct"
        score+=1
    else:
        if guess in guesses:
            recentguess = "incorrect"
            chancesleft -=1
        else:
            recentguess = "incorrect\nalready guessed"
    print(f"Name: {name}")
    print(f"Difficulty: {difficulty[mode]}")
    print(f"Score: {score}")
    print(f"Chances left: {chancesleft}")
    print(f"Guessed letters", guesses)
    print(graphic(chancesleft))
    print(recentguess)

            

