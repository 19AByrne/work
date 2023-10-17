#euler problem 7
def isprime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True
prm = [0,2,3,5,6,11,13]
num = 104729
while len(prm) != 10001:
    num += 1
    if isprime(num) == True:
        print(f"appended {num}")
        print(f"{len(prm)}")
        prm.append(num)
print(prm[-1])