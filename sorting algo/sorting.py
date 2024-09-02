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
    
    for m in range(len(L)):
        smalli = m
        for i in range(m+1,len(L)):
            if L[smalli] > L[i]:
                smalli = i
        L[m], L[smalli] = L[smalli], L[m]
    return L

def bubble(L):
    print(*L, sep=',')
    for p in range(len(L)-1):
        for b in range(len(L)-1):
            if L[b] > L[b+1]:
                L[b], L[b+1] = L[b+1], L[b]
                for x in range(len(L)):
                    if x == b or x == b+1:
                        print(Fore.RED + '[' + str(L[x]) + ']' + Fore.WHITE, end=' ')
                    else:
                        print('[' + str(L[x]), end='] ')
                print()
                    
    return(L)

def simple(L):
    e = []
    for x in range(len(L)):
        si = 0
        for i in range(len(L)):
            if L[i] < L[si]:
                si = i
        e.append(L[si])
        L.remove(L[si])
    return e

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
            print(bubble(user_list))
            
        elif choice2 == 2:
            print('Enter the length of your list')
            length = int(input())
            print('Enter your unsorted list 1 by 1')
            user_list = [int(input()) for x in range(length)]
            print(simple(user_list))
        
        elif choice2 == 3:
            print('Enter the length of your list')
            length = int(input())
            print('Enter your unsorted list 1 by 1')
            user_list = [int(input()) for x in range(length)]
            print(simple_selection(user_list))
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

