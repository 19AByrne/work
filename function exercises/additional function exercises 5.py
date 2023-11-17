#additional function exercises 5
def inrange(num,inpRange):
    fullrange = []
    for x in range(inpRange[0],inpRange[1]+1):
        fullrange.append(x)
    if num in fullrange:
        return True
    else:
        return False
num = 52
Range = (1,12)
if inrange(num,Range) == True:
    print(f"{num} is in range {Range[0]} to {Range[1]}")
else:
    print(f"{num} is not in range {Range[0]} to {Range[1]}")