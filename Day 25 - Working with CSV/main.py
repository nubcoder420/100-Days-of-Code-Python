
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")

# # calculate average temperature
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average_temp = sum(temp_list) / len(temp_list)
# print(round(average_temp, 2))
#
# # using Series.mean()
# print(data["temp"].mean())
#
# # find the max value
# print(data["temp"].max())

### ways of getting data in the columns ###
# print(data["condition"])    # using [], must match*
# print(data.condition)   # treat it as an object

### getting data in a ROW
# print(data[data.day == "Monday"]) # syntax table[column == row]

# print(data[data.temp == data.temp.max()])

# Challenge: convert Monday's temperature from C to F
monday = data[data.day == "Monday"]

def c_to_f(celsius):
    return (celsius * (9/5)) + 32

print(c_to_f(monday.temp))


