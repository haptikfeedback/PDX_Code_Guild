import datetime

path = r'astor.rain'

with open(path, 'r') as file:
    lines = file.readlines()

i = 0
while lines[i].find('-----') < 0:
    i += 1
print(i)

data = []
for i in range(start_line, len(lines)):
    data_line = lines[i].split()
    date = datetime.datetime.strptime(dat)