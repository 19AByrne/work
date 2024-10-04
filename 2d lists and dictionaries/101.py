dic2d = {'John': {'N':3056, 'S':8463, 'E':8441, 'W':2694},
        'Tom': {'N':4832, 'S':6786, 'E':4737, 'W':3612},
        'Anne': {'N':5239, 'S':4802, 'E':5820, 'W':1859},
        'Fiona': {'N':3904, 'S':3645, 'E':8821, 'W':2451}}

for k, v in dic2d.items():
    print(k, *v.items())
    
user_name = str(input('Enter a name: '))
user_region = str(input('Enter a region: '))

new = int(input(f'Enter new value for {dic2d[user_name][user_region]}: ' ))
dic2d[user_name][user_region] = new

for k, v in dic2d.items():
    print(k, *v.items())