from colorama import *
def binary_search(L,t):
    low = 0
    high = (len(L)-1)
    mid = round((low+high)/2)
    if L[low] == t:
        L[mid] = t
    if L[high] == t:
        L[mid] = t
    while L[mid] != t:
        mid = round((low+high)/2)
        if t > L[mid]:
            low = mid
        elif t < L[mid]:
            high = mid
        print(low,high)
    return mid

def simple_selection(L):
    for o in range(len(L)):
        print('[' + f'{L[o]}' + ']',end = ' ')
    print()
    
    for m in range(len(L)):
        print(f'pass {m+1}')
        smalli = m
        for i in range(m+1,len(L)):
            if L[smalli] > L[i]:
                smalli = i
                
        for o in range(len(L)):
            if o == i:
                print(Fore.GREEN + '[' + str(L[o]) + ']' + Fore.WHITE, end=' ')
            elif o == m:
                print(Fore.RED + '[' + str(L[o]) + ']' + Fore.WHITE, end=' ')
            else:
                print('[' + f'{L[o]}' + ']',end = ' ')
        print()
        L[m], L[smalli] = L[smalli], L[m]
        for o in range(len(L)):
            if o == i:
                print(Fore.RED + '[' + str(L[o]) + ']' + Fore.WHITE, end=' ')
            elif o == m:
                print(Fore.GREEN + '[' + str(L[o]) + ']' + Fore.WHITE, end=' ')
            else:
                print('[' + f'{L[o]}' + ']',end = ' ')
        if i == m:
            print(' No Swap')
        print('\n')
    for o in range(len(L)):
        print('[' + f'{L[o]}' + ']',end = ' ')
    print()

def bubble(L):
    for o in range(len(L)):
        print('[' + f'{L[o]}' + ']',end = ' ')
    print('\n')
    for p in range(len(L)-1):
        for b in range(len(L)-1):
            if L[b] > L[b+1]:
                L[b], L[b+1] = L[b+1], L[b]
                swapping = True
            else:
                swapping = False
            for x in range(len(L)):
                if x == b and swapping == 1 or x == b+1 and swapping == 1:
                    print(Fore.GREEN + '[' + str(L[x]) + ']' + Fore.WHITE, end=' ')
                elif x == b and swapping == 0 or x == b+1 and swapping == 0:
                    print(Fore.RED + '[' + str(L[x]) + ']' + Fore.WHITE, end=' ')
                else:
                    print('[' + str(L[x]), end='] ')
                        
            print()
        print(f'end of pass {p+1}\n')
                    
    for o in range(len(L)):
        print('[' + f'{L[o]}' + ']',end = ' ')
    print('\n')
    
def simple(L):
    for o in range(len(L)):
        print('[' + f'{L[o]}' + ']',end = ' ')
    print('\n')
    e = []
    for x in range(len(L)):
        si = 0
        for i in range(len(L)):
            if L[i] < L[si]:
                si = i
        print(f'pass {x+1}')
        print('List:     ', end='')
        for o in range(len(L)):
            if o == si:
                print(Fore.RED + '[' + str(L[o]) + ']' + Fore.WHITE, end=' ')
            else:
                print('[' + f'{L[o]}' + ']',end = ' ')
        e.append(L[si])
        L.remove(L[si])
        print()
        print('New List: ', end='')
        for o in range(len(e)):
            if o == len(e)-1:
                print(Fore.GREEN + '[' + str(e[o]) + ']' + Fore.WHITE, end=' ')
            else:
                print('[' + f'{e[o]}' + ']',end = ' ')
        print('\n')
        
    for o in range(len(e)):
        print('[' + f'{e[o]}' + ']',end = ' ')
    print('\n')

def Linear_search(L,t):
    for i in range(len(L)):
        if L[i] == t:
            return i
        
while 1:
    
    print('''1) sorting
2) searching''')
    choice1 = int(input())
    if choice1 == 1:
        print('''1) Bubble sort
2) Simple sort
3) Simple selection sort''')
        choice2 = int(input())
        if choice2 == 1:
            print('Enter the length of your list')
            length = int(input())
            print('Enter your unsorted list 1 by 1')
            user_list = [int(input()) for x in range(length)]
            bubble(user_list)
            
        elif choice2 == 2:
            print('Enter the length of your list')
            length = int(input())
            print('Enter your unsorted list 1 by 1')
            user_list = [int(input()) for x in range(length)]
            simple(user_list)
        
        elif choice2 == 3:
            print('Enter the length of your list')
            length = int(input())
            print('Enter your unsorted list 1 by 1')
            user_list = [int(input()) for x in range(length)]
            simple_selection(user_list)
    elif choice1 == 2:
        print('''1) Linear search
2) Binary search''')
        choice2 = int(input())
        if choice2 == 1:
            print('Enter the length of your list')
            length = int(input())
            print('Enter your sorted list 1 by 1')
            user_list = [int(input()) for x in range(length)]
            print('Enter your target')
            target = int(input())
            Linear_search(user_list,target)
            
        elif choice2 == 2:
            print('Enter the length of your list')
            length = int(input())
            print('Enter your sorted list 1 by 1')
            user_list = [int(input()) for x in range(length)]
            print('Enter your target')
            target = int(input())
            binary_search(user_list,target)

