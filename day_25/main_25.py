# import csv
#
# with open('weather_data.csv') as data_file:
#     data_csv = csv.reader(data_file)
#     data_list = [row for row in data_csv]
#     temps = []
#     for i in range(1,len(data_list)):
#         t = data_list[i][1]
#         temps.append(int(t))
#     print(temps)

import pandas as pd

data = pd.read_csv('weather_data.csv')
# print(data)
# print(data["temp"])
# data_dict = data.to_dict()
#
# temps = data["temp"]
# print(temps.mean())
# print(temps.max())

# print(data[data["day"] == "Monday"])
# print(type(data[data["day"] == "Monday"]))
# print(data.iloc[5])
# print(type(data.iloc[5]))

# print(data[data.temp == data.temp.max()])

# monday_temp_C = data[data.day == "Monday"].temp
# monday_temp_F = monday_temp_C * 9/5 + 32
# print(monday_temp_F)

data_dict = {
    "students": ["Asia", "Basoa", "Casia"],
    "scores": [54, 12, 99]
}
df = pd.DataFrame(data_dict)
print(df)
df.to_csv("students_scores.csv")













