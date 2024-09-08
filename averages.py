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
    print(f'big = {big},')
    print(L)
    return L[big]

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
        if NL[i] < NL[big]:
            small = i
    return L[small]

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
        print('pass')
        m = Mode(NL)
        top5.append(m)
        print(NL)
        for i in range(NL.count(m)):
            NL.remove(m)
    
    print(top5)
    print('done') 
    
def Last5(L):
    last5 = []
    NL = L.copy()
    for x in range
    
while 1:
    print('Enter the length of your list')
    length = int(input())
    print('Enter your sorted list 1 by 1')
    user_list = [int(input()) for x in range(length)]
    while 1:
        print('''1) Mean
2) Median
3) Mode
4) Frequency
5) Top 5
6) Last 5''')
        input()
        print(Last5([3, 4, 8, 9, 9, 10, 10, 11, 11, 11, 12, 12, 12, 12]))



