#checking if string is palindrome
def palcheck(s):
    floor = len(s) // 2
    div = len(s) / 2
    pal = []
    if floor == div:
        # length is an even number
        for x in range(0,len(s)):
            if x == 0:
                if (s[x]) == (s[-1]):
                    pal.append('T')  
            else:
                if (s[x]) == (s[-1-x]):
                    pal.append('T')         
        if len(pal) == len(s):
            return True
        else:
            return False
    elif floor != div:
        #length is odd number
        for x in range(0,len(s)):
            if x == 0:
                if (s[x]) == (s[-1]):
                    pal.append('T')
            else:
                if (s[x]) == (s[-1-x]):
                    pal.append('T')
                    
                    
        if len(pal) == len(s):
            return True
        else:
            return False
            
string = str(input("Enter any string\n"))
if palcheck(string) == True:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
