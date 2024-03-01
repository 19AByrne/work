def AND(a,b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0
    
def OR(a,b):
    if a + b >= 1:
        return 1
    else:
        return 0
    
def NOT(a):
    if a == 1:
        return 0
    elif a == 0:
        return 1
    
def NOR(a,b):
    return NOT(OR(a,b))

def NAND(a,b):
    return NOT(AND(a,b))

def XOR(a,b):
    if not a == b:
        return 1
    else:
        return 0
    
def XNOR(a,b):
    return NOT(XOR(a,b))




while 1:
    choice = str(input("Type name of gate you want to run: "))
    choice = choice.upper()
    
    x = int(input("Enter value for a: "))
    if not choice == 'NOT':
        y = int(input("Enter value for b: "))
    
    if choice == 'NOT':
        print(NOT(x))
    elif choice == 'AND':
        print(AND(x,y))
    elif choice == 'OR':
        print(OR(x,y))
    elif choice == 'NOR':
        print(NOR(x,y))
    elif choice == 'NAND':
        print(NAND(x,y))
    elif choice == 'XNOR':
        print(XNOR(x,y))
    elif choice == 'XOR':
        print(XOR(x,y))

    
        
