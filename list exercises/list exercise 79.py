#list exercise 79
nums = []
num1 = int(input("Enter a number "))
num2 = int(input("Enter another number "))
num3 = int(input("Enter one more number "))
nums = [num1, num2, num3]
print(*nums, sep=" ")
yn = str(input("Do you still want the last number in the list? "))
if yn == "no":
    nums.remove(nums[-1])
print(*nums, sep=" ")
