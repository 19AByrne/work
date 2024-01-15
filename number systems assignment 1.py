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
    d1 = binarytodecimal(b1)
    d2 = binarytodecimal(b2)
    total = d1 + d2
    total = str(total)
    binarysum = decimaltobinary(total)
    return binarysum

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