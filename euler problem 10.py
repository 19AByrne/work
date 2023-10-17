#euler problem 10
primenumbers = [2]
def isprime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

num = 1
while num < 2000000:
    isprime(num)
    if isprime(num):
        primenumbers.append(num)
    num += 2
    print(num)
print(sum(primenumbers)-1)