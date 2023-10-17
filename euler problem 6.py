#project euler problem 6
nums = []
for x in range(1,101):
    nums.append(x)
    x =+1
print(nums)
sumofsq = 0


for x in range(0, len(nums)):
    sumofsq = sumofsq + nums[x]**2
print(sumofsq)


sqofsum = 0


for x in range(0, len(nums)):
    sqofsum = sqofsum + nums[x]
sqofsum = sqofsum**2
print(sqofsum)

difference = sqofsum - sumofsq
print(difference)