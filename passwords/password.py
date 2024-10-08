def checkpass(p):
    passvalid = False
    para = [False,False,False,False,False]
    if len(p) >= 8:
            para[0] = True
    for c in p:
        if para[1] == False:
            para[1] = c.isupper()
        if para[2] == False:
            para[2] = c.islower()
        if para[3] == False:
            para[3] = c.isdigit()
        if para[4] == False:
            para[4] = c in ['!', '£', '$', '€', '%', '&', '*', '#']
    return all(para)

def get_data(filename):
    file = open(filename, 'r')
    title = file.readline()
    list2d = []
    for line in file:
        line = line.strip('\n')
        list2d.append(line)
    return list2d # function does not make 2d list yet

print(get_data('passwords.csv'))
running = True
while running:
    print('''1) Create a new User ID
2) Change a password
3) Display all user IDs
4) Quit''')
    choice = int(input())
    if choice == 1:
        fr = open('passwords.csv', 'r')
        fa = open('passwords.csv', 'a')
        header = fr.readline()
        new = str(input('Enter new User ID:\n'))
        userids = []
        for line in fr:
            line = line.strip('\n')
            line = line.split(', ')
            userids.append(line[0])
        print(userids)
        while new in userids:
            print('User ID taken')
            new = str(input('Enter new User ID:\n'))    
        
        print('''Passwords must
 - contain atleast 8 characters
 - include uppercase
 - include lowercase
 - include numbers
 - include 1 special character (!, £, $, €, %, &, *, #)''')
        special = ['!', '£', '$', '€', '%', '&', '*', '#']
        newpass = str(input('Enter Password:\n'))
        while not checkpass(newpass):
            print('invalid')
            newpass = str(input('Enter Password:\n'))
        fa.write(f'\n{new}, {newpass}')
        
        fa.close()
        fr.close()
        
    elif choice == 4:
        running = False
        
