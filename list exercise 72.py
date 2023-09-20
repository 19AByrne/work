# list exercise 72
sbj = ["Maths", "Irish", "English", "Computer Science", "DCG", "Construction"]
print(sbj)
disliked = str(input("Which of these subjects do you not like? "))
sbj.remove(disliked)
print(disliked, "will be removed from the list.")
print(sbj)