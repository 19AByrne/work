def binarytodecimal(binary):
    total = 0
    for index, x in enumerate(binary):
        expo = (len(binary)-index-1)
        num = int(x)
        if num:
            num = 1*(2**expo)
            total += num
    return total
        
def decimaltobinary(decimal):
    binary = ''
    decimal = int(decimal)
    while decimal != 0:
        mod = decimal % 2
        mod = str(mod)
        binary = mod + binary
        decimal = decimal // 2
    return binary

def addingbinary(b1,b2):
    b3 = ''
    if len(b1) != len(b2):
        while len(b1) > len(b2):
            b2 = '0' + b2
        while len(b2) > len(b1):
            b1 = '0' + b1
    b1 = '0' + b1
    b2 = '0' + b2
    b1r = b1[::-1]
    b2r = b2[::-1]
#     print(b1r)
#     print(b2r)
    carrying = False
    for i in range(len(b1)):
        if carrying:
            bsum = 1
        else:
            bsum = 0
        b1n = int(b1r[i])
        b2n = int(b2r[i])
        bsum += (b1n+b2n)
#         print(bsum)
        if bsum == 2:
            carrying = True
            bsum = 0
        elif bsum == 3:
            carrying = True
            bsum = 1
        bsum = str(bsum)
        b3 = bsum + b3
    while b3[0] == '0':
        b3 = b3[1:]
    return b3
        
while 1:
    choice = input("binary to decimal(1), decimal to binary(2), or adding binary(3)\n")
    if choice == '1':
        num = str(input("Enter binary: "))
        print(f"Decimal is {binarytodecimal(num)}")
    elif choice == '2':
        num = str(input("Enter decimal: "))
        print(f"Binary is {decimaltobinary(num)}")
    elif choice == '3':
        num1 = str(input("Enter binary num1: "))
        num2 = str(input("Enter binary num2: "))
        print(f"Sum of these nums is {addingbinary(num1,num2)}")
    print()

            
