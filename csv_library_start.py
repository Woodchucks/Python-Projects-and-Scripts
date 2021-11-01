# with open("weather_data.csv") as data:
#     contents = data.readlines()
#     for line in contents:
#         print(line.strip("\n"))

import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] == 'temp':
            pass
        else:
            temperature.append(int(row[1]))
    print(temperature)
