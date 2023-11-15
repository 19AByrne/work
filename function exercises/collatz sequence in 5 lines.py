def collatz(number):
    if number%2: return(3*number+1)
    else: return(number//2) 
user_num = int(input("Enter a number: "))
while user_num != 1: user_num = collatz(user_num); print(user_num)