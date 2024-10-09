def return_data(filename, l):
    file = open(filename, 'w')
    for line in l:
        print(f'{line[0]}, {line[1]}')
        file.write(f'{line[0]}, {line[1]}\n')
    file.close()

def get_data(filename):
    file = open(filename, 'r')
    list2d = []
    for line in file:
        line = line.strip('\n')
        line = line.split(', ')
        list2d.append(line)
    file.close()
    return list2d

def create_userID(newID, list2d):
    for line in list2d:
        if newID == line[0]:
            return False
    return True

def create_password(p):
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

def change_password(userID, newpassword, list2d):
    for line in list2d:
        for x in line:
            if x == userID:
                line[1] = newpassword
            
def display_all_userID(list2d):
    for line in list2d:
        print(*line, sep=', ')

running = True
csv = get_data('passwords.csv')
while running:
    print('''1) Create a new User ID
2) Change a password
3) Display all user IDs
4) Save & Quit''')
    choice = int(input())

    if choice == 1:
        newuserID = str(input('Enter new User ID:\n'))
        while not create_userID(newuserID,csv):
            print('invalid')
            newuserID = str(input('Enter new User ID:\n'))
            
        print('''
Passwords must
 - contain atleast 8 characters
 - include uppercase
 - include lowercase
 - include numbers
 - include 1 special character (!, £, $, €, %, &, *, #)''')
            
        newpassword = str(input('Enter new password:\n'))
        while not create_password(newpassword):
            print('invalid')
            newpassword = str(input('Enter new password:\n'))
            
        csv.append([newuserID,newpassword])

    elif choice == 2:
        selectedID = str(input('Enter the ID you want to change password of:\n'))
        while create_userID(selectedID, csv):
            print('invalid')
            selectedID = str(input('Enter the ID you want to change password of:\n'))
        newuserpassword = str(input('Enter Password:\n'))
        change_password(selectedID, newuserpassword, csv)
        
    elif choice == 3:
        print()
        display_all_userID(csv)
        print()
        
    elif choice == 4:
        print(csv)
        return_data('passwords.csv', csv)
        running = False
        
