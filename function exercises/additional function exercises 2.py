#additional function exercises 2
def multiply(nums):
    total = 1
    for x in range(len(nums)):
        total *= nums[x]
    return total
list = [8,2,3,-1,7]
print(multiply(list))