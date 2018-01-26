import datetime

path = r'astor.rain'

def parse_file(path):

    with open(path, 'r') as file:
        lines = file.readlines()

    start_line = 0
    while '----' not in lines[start_line]:
        start_line += 1
    start_line += 1

    data = []
    for i in range(start_line, len(lines)):
        data_line = lines[i].split()
        date = datetime.datetime.strptime(data_line[0], '%d-%b-%Y')
        daily_rainfall = int(data_line[1]) if data_line[1] != '-' else None
        data.append((date, daily_rainfall))
        rainAverage = sum(daily_rainfall)
        # rainAverage = lambda dailyAverage: sum(daily_rainfall) / len(daily_rainfall)
        # for daily_rainfall in sorted(daily_rainfall, key=rainAverage, reverse=True):
        #     print(date, "Average: ", rainAverage(date))

        print(rainAverage)
    return data


data = parse_file(path)

print(data)
