# task 9 q3
s1 = str(input("Enter a word "))
s2 = str(input("Enter another word "))
s3 = s1[:(len(s1)//2)]+s2+s1[(len(s1)//2):]
print(s3)