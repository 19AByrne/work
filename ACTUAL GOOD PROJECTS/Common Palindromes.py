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
"""))

userrange = int(input("""
What is the range you would like to check for palindromes:
"""))

nlist = []
for x in range(userrange):
    nlist.append(x)
    
    
def palindromes_Decimal_Binary():
    """prints numbers palindromic in ***decimal*** and ***binary***"""
    palindromes_in_base10 = [x for x in nlist if pc(x) == True]
    binary_of_every_palindrome_in_base10 = [decimaltobinary(x) for x in palindromes_in_base10 if pc(decimaltobinary(x)) == True]
    decimal_of_every_palindrome_in_base10_and_base2 = [binarytodecimal(str(x)) for x in binary_of_every_palindrome_in_base10]
    
    paldict = {k:v for k,v in zip(decimal_of_every_palindrome_in_base10_and_base2, binary_of_every_palindrome_in_base10)}
    print("base10 : base2\n--------------")
    for x in paldict:
        print(f"{x} : {paldict[x]}")
        

def palindromes_Decimal_Hexadecimal():
    """prints numbers palidnromic in ***decimal*** and ***hexadecimal***"""
    palindromes_in_base10 = [x for x in nlist if pc(x) == True]
    hexa_of_every_palindrome_in_base10 = [decimaltohexa(x) for x in palindromes_in_base10 if pc(decimaltohexa(x)) == True]
    decimal_of_every_palindrome_in_both_base10_and_base16 = [hexatodecimal(str(x)) for x in hexa_of_every_palindrome_in_base10]
    
    paldict = {k:v for k,v in zip(decimal_of_every_palindrome_in_both_base10_and_base16, hexa_of_every_palindrome_in_base10)}
    print("base10 : base16\n---------------")
    for x in paldict:
        print(f"{x} : {paldict[x]}")


def palindromes_Hexadecimal_Binary():
    """prints numbers palindromic in ***hexadecimal*** and ***binary***"""
    nlist_in_base2 = [decimaltobinary(x) for x in nlist if pc(decimaltobinary(x)) == True]
    hexa_of_every_palindrome_in_base2 = [binarytohexa(x) for x in nlist_in_base2 if pc(binarytohexa(x)) == True]
    binary_of_every_palindrome_in_base16 = [hexatobinary(x) for x in hexa_of_every_palindrome_in_base2]

    paldict = {k:v for k,v in zip(binary_of_every_palindrome_in_base16, hexa_of_every_palindrome_in_base2)}
    print("base2 : base16\n---------------")
    for x in paldict:
        print(f"{x} : {paldict[x]}")
    


if choice == 1:
    palindromes_Decimal_Binary()
elif choice == 2:
    palindromes_Decimal_Hexadecimal()
elif choice == 3:
    palindromes_Hexadecimal_Binary()

