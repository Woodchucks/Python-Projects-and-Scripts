# with open("weather_data.csv") as data:
#     contents = data.readlines()
#     for line in contents:
#         print(line.strip("\n"))

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] == 'temp':
#             pass
#         else:
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# temp_list = data["temp"].to_list()

# average_temp = sum(temp_list)/ len(temp_list)
# print(round(average_temp, 2))

# average_temp = data["temp"].mean()
# print(round(average_temp, 2))
# print(data["temp"].max())
#
# print(data[data.temp == data.temp.max()])
#
# Monday = data[data.day == "Monday"]
# print((Monday.temp * 1.8) + 32)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
fur_color_list = fur_color.to_list()

# gray = 0
# black = 0
# cinnamon = 0
#
# for color in fur_color_list:
#     if color == "Gray":
#         gray += 1
#     if color == "Black":
#         black += 1
#     if color == "Cinnamon":
#         cinnamon += 1

grey = len(data[fur_color == "Gray"])
black = len(data[fur_color == "Black"])
cinnamon = len(data[fur_color == "Cinnamon"])

data_collection_fur = {
    "Fur Color": ["Grey", "Black", "Cinnamon"],
    "Count": [grey, black, cinnamon]
}
squirrel = pandas.DataFrame(data_collection_fur)
squirrel.to_csv("new_file.csv")
