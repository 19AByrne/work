def fac(n):
    if n <= 1:
        return 1
    else: return n * fac(n-1)
    
print(fac(6))

# may possible work

# def alternatifefac(n):
#     if n<=1:
#         return 1
#     else:
#         rest = fac(n-1)
#         return rest