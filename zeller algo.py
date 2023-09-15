#exercise 6
dd = int(input("enter a date: "))
mm = str(input("enter a month as: "))
year = int(input("enter a year: "))
y = (year % 100)
c = (y - year)/-100
c = int(c)
i
if mm == 'january':
    mm = (13)
    
if mm == ('february'):
    mm = int(14)
    
if mm == ('march'):
    mm = int(3)
    
if mm == ('april'):
    mm = int(4)
    
if mm == ('may'):
    mm = int(5)
    
if mm == ('june'):
    mm = int(6)
    
if mm == ('july'):
    mm = int(7)
    
if mm == ('august'):
    mm = int(8)
    
if mm == ('september'):
    mm = int(9)
    
if mm == ('october'):
    mm = int(10)
    
if mm == ('november'):
    mm = int(11)
    
if mm == ('december'):
    mm = int(12)
    

(w) = dd + 13*(mm+1)//5 + (y) + (y/4) + (c/4) - (2*c)
w = int(w)
w = w%7

if w == 2:
    w = str('Monday')
    
if w == 3:
    w = str('Tuesday')
    
if w == 4:
    w = str('Wednesday')
    
if w == 5:
    w = str('Thursday')
    
if w == 6:
    w = str('Friday')
    
if w == 0:
    w = str('Saturday')
    
if w == 1:
    w = str('Sunday')
    

print(w)