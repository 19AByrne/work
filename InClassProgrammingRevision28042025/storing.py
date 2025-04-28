f = open('Data.csv', 'r')
headers = f.readline()
headers = headers.strip('\n')
headers = headers.split(',')

dictionary = {}
for line in f:
    line = line.strip('\n')
    line = line.split(',')
    for i,x in enumerate(line):
        dictionary[ headers[i] ] = x
    
print(dictionary)
# for x in headers:
#     print(f'Enter your {x}')
#     user_inputs.append(input())
