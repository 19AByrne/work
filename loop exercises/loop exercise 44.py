#loop exercise 44
count = int(input("How many people do you want to invite? "))
if count <= 10:
    for x in range(0,count):
        name = str(input("Tell me someone whos invited. "))
        print(f"{name} has been invited")
elif count > 10:
    print("too many people.")
