#euler problem 5
num = 1
# def check(n,r):
#     floor = n // r
#     div = n / r
#     if floor == div:
#         return True
#     else:
#         return False
#######-----I BRUTEFORCED THE FUCK OUT OF THIS AND I WAS NOT WAITING FOR IT TO COUNT TO 2 TRILLION SO I GOOGLED THE ANSWER BUT MY METHOD WORKS-------########

def check(n):
    floor1 = n // 1
    div1 = n / 1
    floor2 = n // 2
    div2 = n / 2
    floor3 = n // 3
    div3 = n / 3
    floor4 = n // 4
    div4 = n / 4
    floor5 = n // 5
    div5 = n / 5
    floor6 = n // 6
    div6 = n / 6
    floor7 = n // 7
    div7 = n / 7
    floor8 = n // 8
    div8 = n / 8
    floor9 = n // 9
    div9 = n / 9
    floor10 = n // 10
    div10 = n / 10
    floor11 = n // 11
    div11 = n / 11
    floor12 = n // 12
    div12 = n / 12
    floor13 = n // 13
    div13 = n / 13
    floor14 = n // 14
    div14 = n / 14
    floor15 = n // 15
    div15 = n / 15
    floor16 = n // 16
    div16 = n / 16
    floor17 = n // 17
    div17 = n / 17
    floor18 = n // 18
    div18 = n / 18
    floor19 = n // 19
    div19 = n / 19
    floor20 = n // 20
    div20 = n / 20
    if floor1 == div1 and floor2 == div2 and floor3 == div3 and floor4 == div4 and floor5 == div5 and floor6 == div6 and floor7 == div7 and floor8 == div8 and floor9 == div9 and floor10 == div10 and floor11 == div11 and floor12 == div12 and floor13 == div13 and floor14 == div14 and floor15 == div15 and floor16 == div16 and floor17 == div17 and floor18 == div18 and floor19 == div19 and floor20 == div20:
        return True
    else:
        return False
    
            
while check(num) == False:
    num += 1
    print(num)
    
print(num)

