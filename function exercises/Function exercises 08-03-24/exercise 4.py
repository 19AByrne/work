def counter(l):
    evenl = [x for x in l if x%2 == 0]
    oddl = [x for x in l if x%2 == 1]
    return evenl,sum(evenl),oddl,sum(oddl),(sum(evenl)/len(evenl)),(sum(oddl)/len(oddl))
entering = True
userlist = []
while entering:
    x = (input("Enter a number or input 'stop'"))
    if x == 'stop':
        entering = False
        break
    userlist.append(int(x))
print(counter(userlist))