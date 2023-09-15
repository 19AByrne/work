#exercise 6.2
dd = int(input("enter a date: "))
mm = int(input("enter a month as a number: "))
year = int(input("enter a year: "))
y = (year % 100)
c = (y - year)/-100

c = int(c)
if mm < 3:
    mm = mm+12
    y = y-1
(w) = dd + 13*(mm+1)//5 + (y) + (y//4) + (c//4) - (2*c)
w = w%7
wd = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(wd[w])
