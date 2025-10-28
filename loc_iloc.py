import numpy as np
import pandas as pd

df = pd.read_csv("E:\PureLogics\\dataset_for_prac\\50_Startups.csv", nrows=5)
df = df.loc[[0]]
# print(df)

df = df.loc[0, "State"]
# print(df)

df = pd.read_csv("E:\PureLogics\\dataset_for_prac\\50_Startups.csv", nrows=5)
df = df.loc[0:4, "State"]
# print(df)

df = pd.read_csv("E:\PureLogics\\dataset_for_prac\\50_Startups.csv", nrows=5)
df = df.loc[df["Profit"] > 191792.06]
# print(df)

df = pd.read_csv("E:\PureLogics\\dataset_for_prac\\50_Startups.csv", nrows=5)
df = df.iloc[:, 0]
print(df)
