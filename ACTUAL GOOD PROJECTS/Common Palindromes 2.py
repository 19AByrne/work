def pc(number):
    string = str(number)
    rstr = string[::-1]
    if rstr == string:
        return True
    else:
        return False
    
def decimaltobinary(decimal):
    binary = ''
    decimal = int(decimal)
    while decimal != 0:
        mod = decimal % 2
        mod = str(mod)
        binary = mod + binary
        decimal = decimal // 2
    return binary

def binarytodecimal(binary):
    total = 0
    for index, x in enumerate(binary):
        expo = (len(binary)-index-1)
        num = int(x)
        if num:
            num = 1*(2**expo)
            total += num
    return total

def decimaltohexa(decimal):
    hexa = ''
    hexalist = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
    decimal = int(decimal)
    while decimal != 0:
        mod = decimal % 16
        mod = str(mod)
        if mod in hexalist:
            mod = hexalist[mod]
        hexa = mod + hexa
        decimal = decimal // 16
    return hexa

def hexatodecimal(hexa):
    total = 0
    hexalist = {'A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'15'}
    for index, x in enumerate(hexa):
        if x in hexalist:
            x = hexalist[x]
        expo = (len(hexa)-index-1)
        num = int(x)
        if num > 0:
            num = num*(16**expo)
            total += num
    return total

def binarytohexa(binary):
    hexa = ''
    hexalist = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
    while len(binary) % 4:
        binary = '0' + binary
    while len(binary) > 0:
        selected = binary[:4]
        binary = binary[4:]
        hexanum = str(binarytodecimal(selected))
        if hexanum in hexalist:
            hexanum = hexalist[hexanum]
        hexa = hexa + hexanum
    return hexa

def hexatobinary(hexa):
    binary = ''
    hexalist = {'A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'15'}
    hexa = list(hexa)
    for num in hexa:
        if num in hexalist:
            num = hexalist[num]
        binarysection = decimaltobinary(num)
        while len(binarysection) % 4:
            binarysection = '0' + binarysection
        binary = binary + binarysection
    
    if binary != '':    
        while binary[0] == '0':
            binary=binary[1:]
    return binary

choice = int(input("""
Would You like to see common palindromes in:
1) Base 10 & Base 2
2) Base 10 & Base 16
3) Base 16 & Base 2
4) all
"""))
     
def palindromes_Decimal_Binary():
    num = 0
    while 1:
        if pc(num) == True and pc(decimaltobinary(num)) == True:
            print(f"{num} : {decimaltobinary(num)}")
        num += 1

def palindromes_Decimal_Hexadecimal():
    num = 0
    while 1:
        if pc(num) == True and pc(decimaltohexa(num)) == True:
            print(f"{num} : {decimaltohexa(num)}")
        num += 1


def palindromes_Hexadecimal_Binary():
    num = 0
    while 1:
        if pc(decimaltohexa(num)) == True and pc(decimaltobinary(num)) == True:
            print(f"{decimaltohexa(num)} : {decimaltobinary(num)}")
        num += 1
    
def palindromes_all():
    num = 0
    while 1:
        if pc(num) == True and pc(decimaltobinary(num)) == True and pc(decimaltohexa(num)) == True:
            print(f"{num} : {decimaltobinary(num)} : {decimaltohexa(num)}")
        num += 1
        
        
if choice == 1:
    palindromes_Decimal_Binary()
elif choice == 2:
    palindromes_Decimal_Hexadecimal()
elif choice == 3:
    palindromes_Hexadecimal_Binary()
elif choice == 4:
    palindromes_all()


