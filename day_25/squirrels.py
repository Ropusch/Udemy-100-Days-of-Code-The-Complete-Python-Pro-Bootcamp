import pandas as pd
import numpy as np

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

df = pd.DataFrame(columns=["fur color", "count"])

possible_colors = data["Primary Fur Color"].unique()
possible_colors = possible_colors[~pd.isna(possible_colors)]    #usuwanie nan

for color in possible_colors:
    count = len(data[data["Primary Fur Color"] == color])
    df.loc[len(df)] = [color, count]

print(df)
df.to_csv("color_count.csv")

