import datetime

path = r'astor.rain'

with open(path, 'r') as file:
    lines = file.readlines()

i = 0
while lines[i].find('-----') < 0:
    i += 1
print(i)


data_line = lines[i].split(' ')

data_lines = [datum for datum in data_line if datum != '']

print(data_line)