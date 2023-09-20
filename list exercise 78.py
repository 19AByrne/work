#list exercise 78
tv = ["Atlanta", "Better Call Saul", "Modern Family", "It's Always Sunny in Philadelphia"]
print(tv[0])
print(tv[1])
print(tv[2])
print(tv[3])
usershow = str(input("Enter another show. "))
tv.append(usershow)
tv.sort()
print(*tv, sep=", ")