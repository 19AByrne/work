# question 16(a)
from random import choice

fruits = ['apple', 'cherry', 'orange']

random_fruit_1 = choice(fruits)
random_fruit_2 = choice(fruits)
random_fruit_3 = choice(fruits)

# (i)
print(f'Random Fruit 1: {random_fruit_1}')

# (ii)
print(f'Random Fruit 2: {random_fruit_2}')
print(f'Random Fruit 3: {random_fruit_3}')

print()

# (iii)
if random_fruit_1 == 'cherry':
    print('First fruit is cherry')
    
# (iv)
if random_fruit_1 == random_fruit_2:
    print('First pair match')
    
# (v)    
if random_fruit_1 == random_fruit_2 and random_fruit_1 == 'cherry':
    print('First pair are cherries')
    
# (vi)
if random_fruit_1 in [random_fruit_2,random_fruit_3] or random_fruit_2 in [random_fruit_1,random_fruit_3]:
    print('Matching pair')
    
    
# (vii)
print()

apple_count = 0
cherry_count = 0
orange_count = 0
for i in range(100):
    random_fruit = choice(fruits)
    if random_fruit == 'apple':
        apple_count += 1
    elif random_fruit == 'cherry':
        cherry_count += 1
    else:
        orange_count += 1
    
print(f'''apple {apple_count}
cherry {cherry_count}
orange {orange_count}''')