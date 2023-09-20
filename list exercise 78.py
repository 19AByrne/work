#list exercise 78
tv = ["Atlanta", "Better Call Saul", "Modern Family", "It's Always Sunny in Philadelphia"]
for x in tv:
    print(x)
usershow = str(input("Enter another show. "))
tv.append(usershow)
tv.sort()
print(*tv, sep=", ")
