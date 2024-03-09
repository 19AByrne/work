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

def strtoUTF(string):
    output = ''
    for i in string:
        x = decimaltobinary(ord(i))
        if len(x) <= 7:
            while len(x) != 7:
                x = '0' + x
            output = output + ('0'+x)
        
        if len(x) <= 11 and len(x) > 7:
            while len(x) != 11:
                x = '0' + x
            output = output + ('110'+x[:5]+'10'+x[5:])
        
        if len(x) <= 16 and len(x) > 11:
            while len(x) != 16:
                x = '0' + x
            output = output + ('1110'+x[:4]+'10'+x[4:10]+'10'+x[10:])
        
        if len(x) <= 21 and len(x) > 16:
            while len(x) != 21:
                x = '0' + x
            output = output + ('11110'+x[:3]+'10'+x[3:9]+'10'+x[9:15]+'10'+x[15:])
    return output


def UTFtoString(utf):
    chars = []
    while len(utf) > 0:
        onecount = 0
        for x in utf:
            if x == '1':
                onecount += 1
            if x == '0':
                break
        if onecount == 0:
            onecount = 1
        char = utf[0:(8*onecount)]
        splitchar = []
        for x in range(8,onecount*8+8,8):
            y = x - 8
            splitchar.append(char[y:x])
        splitchar = [(x.lstrip('1'))[1:] for x in splitchar]
        splitchar = binarytodecimal(''.join(splitchar))
        chars.append(chr(splitchar))
        utf = utf[onecount*8:]
    output = ' '.join(chars)
    return output
        
# print(UTFtoString('11110000100111111000111010110101'))
# print(strtoUTF('🎵'))

while 1:
    choice = int(input("""1)UTF-8 to string
2)string to UTF-8
"""))
    if choice == 1:
        userUTF = str(input("Enter UTF-8 binary:\n"))
        print(UTFtoString(userUTF))
    elif choice == 2:
        userString = str(input("Enter Character:\n"))
        print(strtoUTF(userString))
    
    print()


"""6
111000101000001010101100 = €
111011011001010110011100 = 한
00100100 = $
11110000100111111000111010110101 = 🎵
"""










