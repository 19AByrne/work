list2d = [ [2,5,8], [3,7,4], [1,6,9], [4,2,0] ]
print(*list2d, sep='\n')
user_row  = int(input('Enter selected row: '))
user_value = int(input('Enter new value: '))
list2d[user_row].append(user_value)
print(list2d[user_row])
print(*list2d, sep='\n')