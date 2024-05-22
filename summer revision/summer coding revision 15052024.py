##q1
# numlist = [int(input(f'enter number {x}: ')) for x in range(1,6)]
# print(numlist)
# numlist = [x+1 for x in numlist]
# print(numlist)

##q2
# Hours = [12,7,9,9,6,8,2]
# Hours = [x*0.5*1.35 for x in Hours]
# print(round(sum(Hours),1))

##q3
# rainfall = [float(input('How much rainfall was there today in cm: ')) for x in range(7)]
# avg = sum(rainfall)/len(rainfall)
# total = sum(rainfall)
# print(f'average rainfall throughout the week: {avg}')
# print(f'total rainfall throughout the week: {total}')
# days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# for i,day in enumerate(rainfall):
#     if day > 3.5:
#         exceeding = round(day-3.5,1)
#         print(f'on {days[i]} the rainfall exceeded 3.5 by {exceeding}!')

##q4
staff = []
value = []
print('***Welcome***');print()
print('Please choose an option below:')
print('''1. Enter sales data
2. View total sales to date
3. View maximum sale value of any staff member
4. View minimum sale of any staff member
5. View average sale of any staff member''')
choice = int(input())
if choice == 1:
    staff.append(input('Enter member of staffs name: '))
    value.append(input(f'Enter the value sale made by {staff[-1]}: '))
elif choice == 2:
    for i,x in enumerate(staff):
        print(f'{x} : {value[i]}')
elif choice == 3:
    
    
