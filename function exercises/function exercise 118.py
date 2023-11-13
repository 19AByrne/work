#function exercises 118
def getnum():
    num = int(input("Enter a number\n"))
    return num

gnum = getnum()

def count(n):
    for x in range(0,n+1):
        print(x)
    
count(gnum)
