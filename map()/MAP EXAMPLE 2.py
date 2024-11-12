list_o_int=[1,2,3]
b=[4,5,6]
c=[7,8,9]

def return_me_a_total(x,y,z):
    return x+y+z

result = list(map(return_me_a_total,list_o_int,b,c))
print(result)