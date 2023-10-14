#list exercise 78
tv = ["Atlanta", "Better Call Saul", "Modern Family", "It's always sunny in philadelphia"]
print(*tv, sep="\n")
show = str(input("Enter another show\n"))
pos = int(input("What position do you want it in out of 5?\n"))
tv.insert(pos, show)
print(*tv, sep="\n")
