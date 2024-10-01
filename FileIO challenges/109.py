while 1:
    print('''1) Create a new file
2) Display a file
3) Add a new item to the file
Make a selection 1, 2, or 3:''')
    choice = int(input())
    v = [1,2,3]
    while choice not in v:
        print('invalid')
        choice = int(input())

    if choice == 1:
        print('enter a school subject:')
        inp = str(input())
        f = open('subjects.txt', 'w')
        f.write(inp)
        f.close()
    elif choice == 2:
        f = open('subjects.txt', 'r')
        for l in f:
            print(l)
        f.close()
    elif choice == 3:
        f = open('subjects.txt', 'a')
        print('enter a new school subject:')
        inp = str(input())
        f.write(f', {inp}')
        f.close()
