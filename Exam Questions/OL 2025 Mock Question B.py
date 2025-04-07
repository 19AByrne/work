#Question_16_B_OL
#Enter your name here: Aaron Byrne
import random
print("Your options are as follows: d4, d6, d12, and d20")
n = int(input("Which type of dice do you want? 4, 6, 12, or 20: "))
if n in [4,6,12,20]:
    print(f'You will roll a {n}-sided dice')
    print(f'The roll was: {random.randint(1,n)}')
else:
    print(f'You made an incorrect choice')