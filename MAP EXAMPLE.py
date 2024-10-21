list_o_int = ['1','2','3']

def return_me_an_int(x):
    return int(x)

print(list_o_int)
result = list(map(return_me_an_int,list_o_int))
print(result)