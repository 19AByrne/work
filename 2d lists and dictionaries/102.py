dic2d = {}
for x in range(4):
    name = str(input(f'Enter person {x+1}: '))
    size = float(input(f'Enter their shoe size: '))
    age = int(input(f'Enter their age: '))
    dic2d[name] = {'age':age, 'size':size}
    
for k, v in dic2d.items():
    print(k, *v.items())
    