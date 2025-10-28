import numpy as np
import pandas as pd

df = pd.read_csv("E:\\PureLogics\\dataset_for_prac\\50_Startups.csv",
                 nrows=5,)

df = df.replace(to_replace="Florida", value="Canada")
# print(df)

df = df.replace("Florida", "New York")
# print(df)

df = df.replace([136897.80, 151377.59, 101145.55, 118671.85, 91391.77], "none")
# print(df)

df = pd.read_csv("E:\\PureLogics\\dataset_for_prac\\50_Startups.csv",
                 nrows=5,)
df = df.replace({"Administration": 136897.80, }, 0)
# print(df)


df = pd.read_csv("E:\\PureLogics\\dataset_for_prac\\50_Startups.csv",
                 nrows=5,)
df = df.replace("New York", method="ffill")
print(df)


# df.replace(1, 100)                                                  Replace all 1s with 100
# df.replace([1, 2], [100, 200])                                      Replace multiple values
# df.replace({'A': 1, 'B': 'apple'}, {'A': 100, 'B': 'mango'})        Replace using dict
# df.replace(to_replace='a.*', value='fruit', regex=True)             Replace using regex pattern
# df.replace(0, None, inplace=True)                                   Replace directly in the original DataFrame
# df.replace({'A': [1, 2]}, 99, limit=1)                              Limit replacements to 1 occurrence per column
# df.replace(np.nan, 0)                                               Replace NaN with 0
