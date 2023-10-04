#while exercise 51
num = 10
while num != 0:
    print(f"There are {num} green botles hanging on the wall, {num} green bottles hanging on the wall, and if 1 green bottle should accidentally fall")
    num -=1
    guess = int(input("How many green bottles are hanging on the wall? "))
    while guess != num:
        print(f"incorrect try again")
        guess = int(input("How many green bottles are hanging on the wall? "))
print("There are no more green bottles hanging on the wall")