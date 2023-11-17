#additional function exercises 8
def isprime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

print(isprime(6))