#question 16 (b)
#ajb 230575

from random import choice

fruits = ['apple', 'cherry', 'orange']

print(f'The initial list of fruits is:\n{fruits}\n')

user_fruit = str(input('Enter an additional fruit: '))
fruits.append(user_fruit)

print(f'The list of four fruits is: \n{fruits}\n')

winning_fruit = str(input('Nominate your winning fruit: '))
while not winning_fruit in fruits:
    print('Error: winning fruit must be in the list')
    winning_fruit = str(input('Nominate your winning fruit: '))

print()
    
print(f'The winning fruit you selected is {winning_fruit}')

print()


tries = 1
won = False
while not won:
    random_fruit_1 = choice(fruits)
    random_fruit_2 = choice(fruits)
    random_fruit_3 = choice(fruits)
    if random_fruit_1 == winning_fruit and random_fruit_2 == winning_fruit and random_fruit_3 == winning_fruit:
        won = True
        break
    else:
        tries += 1

print(f'Winner after {tries} tries')