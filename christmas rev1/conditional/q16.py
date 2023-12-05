n = int(input("How many numbers would you like to enter: "))
nums = []
for x in range(1,n+1):
    num = int(input(f"{x}:Enter a positive number: "))
    while num < 0:
        print("error")
        num = int(input(f"{x}:Enter a POSITIVE number: "))
    nums.append(num)
Sum = 0
for x in nums:
    Sum += x
mean = Sum/(len(nums))

print(nums)
print(Sum)
print(mean)