#Questio_16_A_OL
#Enter your name here: Aaron Byrne

value_small_containers = 0.15

number_small_containers = int(input("Please enter how many small containers you are returning: "))

print(f'The total value of your small containers was : € {number_small_containers*value_small_containers}')

value_large_containers = 0.25

number_large_containers = int(input("Please enter how many large containers you are returning: "))

print(f'The total value of your large containers was: € {number_large_containers*value_large_containers}')

grand_total = (value_large_containers*number_large_containers) + (number_small_containers*value_small_containers)
print(f'Your grand total was: € {grand_total}')

user_bill = float(input('Please enter your shopping bill: '))
print(f'Your shopping bill with the desposit return is: € {user_bill-grand_total}')