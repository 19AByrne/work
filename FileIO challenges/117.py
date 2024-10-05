import random
user_score = 0
name = str(input('Enter your name: '))
num1 = random.randint(-10,10)
num2 = random.randint(-10,10)
ans1 = num1+num2
num3 = random.randint(-15,15)
num4 = random.randint(-15,15)
ans2 = num3+num4
f = open('score.csv', 'a')
user_ans1 = int(input(f'({num1}) + ({num2}) = '))
user_ans2 = int(input(f'({num3}) + ({num4}) = '))
if user_ans1 == ans1:
    user_score += 1
if user_ans2 == ans2:
    user_score += 1
f.write(f'\n{name}, ({num1}) + ({num2}) & ({num3}) + ({num4}), {user_score}')
f.close()