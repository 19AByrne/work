list2d = [ [2,5,8], [3,7,4], [1,6,9], [4,2,0] ]
print(*list2d, sep='\n')
user_row  = int(input('Enter selected row: '))
user_column = int(input('Enter selected column: '))
print(list2d[user_row][user_column])
yn = str(input('Would you like to change this value?: (y/n) '))
v = ['y','n']
while not yn in v:
    print('invalid')
    yn = str(input('Would you like to change this value?: (y/n) '))
    
if yn == 'y':
    new = int(input('Enter new value: '))
    list2d[user_row][user_column] = new

print(*list2d, sep='\n')