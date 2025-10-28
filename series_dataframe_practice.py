import numpy as np
import pandas as pd


def series():
    series = pd.Series([0, 9, 8, 7, 6, 5, 4])
    series_two = pd.Series([0, 9, 8])
    series_three = series + series_two
    series_four = series_three.max()

    print(series_three)
    print(series_four)
    print(series[0:4])


df_list = [0, 9, 8, 7, 6, 5]
df_one = pd.DataFrame(df_list)
# print(df_one)

df_list = {"id": [1, 2, 3, 4], "name": ["Haris", "harry", "har", "ha"]}
df_one = pd.DataFrame(df_list)
# print(df_one)

df_list = [{"id": 1, "name": "haris"}, {"id": 2, }]
df_one = pd.DataFrame(df_list)
print(df_one)
