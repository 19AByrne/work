#function exercise 121
import time
t = time
sl = 0.3
names = []
def Add(l):
    n = str(input("What name would you like to add.\n"))
    l.append(n)
    print("\n")
    t.sleep(sl)
def Change(l):
    choice = str(input(f"Which name would you like to change?\n{l}\n"))
    choiceidx = l.index(choice)
    l.remove(choice)
    n = str(input("What would you like to change it to?\n"))
    l.insert(choiceidx, n)
    print("\n")
    t.sleep(sl)
def Del(l):
    choice = str(input(f"Which name would you like to delete\n{l}\n"))
    l.remove(choice)
    print("\n")
    t.sleep(sl)
def View(l):
    print("\n")
    print(*l, sep='\n')
    print("\n")
    t.sleep(sl)
def program():
    mode = int(input("Select a Mode. \n1) Add a name \n2) Change a name \n3) Delete a name \n4) View list\n5) End Program \nEnter: "))
    if mode == 1:
        Add(names)
    elif mode == 2:
        Change(names)
    elif mode == 3:
        Del(names)
    elif mode == 4:
        View(names)
    elif mode == 5:
        return 'End'
    else:
        print("Invalid answer, Select again!")
    
    
while program() != 'End':
    pass
print("Goodbye!")

