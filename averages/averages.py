f = open('inputlist.txt', 'r')
for line in f:
    user_list = line.split(',')
    
user_list = [int(x) for x in user_list]
user_list.sort()


def Mean(L):
    return (sum(L))/(len(L))

def Mode(L):
    NL=[]
    for x in range(len(L)):
        NL.append(0)
    for x in range(len(L)):
        xcount = 0
        for y in L:
            if y == L[x]:
                xcount+=1
            else:
                pass
        NL[x] = xcount
    big = 0
    for i in range(len(L)):
        if NL[i] > NL[big]:
            big = i
    return L[big]

def Median(L):
    return L[round(len(L)/2)+1] 

def Frequency(L,t):
    count = 0
    for x in L:
        if x == t:
            count += 1
    return count

def Top5(L):
    top5 = []
    NL = L.copy()
    for x in range(5):
        m = Mode(NL)
        top5.append(m)
        for i in range(NL.count(m)):
            NL.remove(m)
    return top5
    
def antimode(L):
    NL=[]
    for x in range(len(L)):
        NL.append(0)
    for x in range(len(L)):
        xcount = 0
        for y in L:
            if y == L[x]:
                xcount+=1
            else:
                pass
        NL[x] = xcount
    
    small = 0
    for i in range(len(L)):
        if NL[i] < NL[small]:
            small = i

    return L[small]
    
def Last5(L):
    lengthvariable = len(L)
    last5 = []
    NL = L.copy()
    for x in range(5):
        m = antimode(NL)
        last5.append(m)
        for i in range(NL.count(m)):
            NL.remove(m)
    return last5
    
while 1:
#     print('Enter the length of your list')
#     length = int(input())
#     print('Enter your sorted list 1 by 1')
#     user_list = [int(input()) for x in range(length)]
    while 1:
        print('''1) Mean
2) Median
3) Mode
4) Frequency
5) Top 5
6) Last 5''')
        choice = int(input())
        if choice == 1:
            print(Mean(user_list))
        elif choice == 2:
            print(Median(user_list))
        elif choice == 3:
            print(Mode(user_list))
        elif choice == 4:
            target = int(input('Enter target value:\n'))
            print(Frequency(user_list,target))
        elif choice == 5:
            print(Top5(user_list))
        elif choice == 6:
            print(Last5(user_list))
        
        input()


