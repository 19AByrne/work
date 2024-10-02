list2d = [ [2,5,8], [3,7,4], [1,6,9], [4,2,0] ]
print(*list2d, sep='\n')

user_row = int(input('Enter row: '))
user_col = int(input('Enter column: '))

print(list2d[user_row][user_col])