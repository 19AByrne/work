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
        return L[round(len(L)/2)] # cheeeeck
    
    
def Frequency(L,t):
    count = 0
    for x in L:
        if x == t:
            count += 1
    return count

def Top5(L):
    pass
    
def Last5(L):
    pass
    
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
    if int(input()) == 1:
        Mean(user_list)
