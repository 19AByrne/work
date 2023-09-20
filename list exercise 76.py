#list exercise 76
name1 = str(input("Who is the first person you are inviting? "))
name2 = str(input("Who is being invited after them? "))
name3 = str(input("And who are you inviting after them? "))
invited = [name1, name2, name3]
yn = input("Do you want to invite anymore people? ")
def func():
    if yn == "Yes":
        
        name4 = str(input("Who else is being invited? "))
        ny = input("Do you want to invite anyone else? ")
        invited.append(name4)
        if ny == "Yes":
            func()
        else:
            print("Okay, You have invited",len(invited), "people")
            print("This is who is invited",invited)
    else:
        print("Okay, You have invited",len(invited), "people")
        print("This is who is invited",invited)
func()
