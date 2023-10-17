#euler problem 5
def check(n, i):
    if (n / i) == (n // i):
        return True
    else:
        return False
num = 0
b = 1
while check(num, b) == False:
    while b != 10:
        check(num, b)
        b =+ 1
print