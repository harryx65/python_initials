import numpy as np
import pandas as pd
import os

# file = pd.read_csv("E:\\python\\data.csv")
# print(file)
# print(file.columns)
# print(os.getcwd())

# file = pd.read_csv("E:\\python\\data.csv", nrows=2)
# file = pd.read_csv("E:\\python\\data.csv", usecols=[
#                    0, 1], skiprows=[3], index_col="Offer Title")
file = pd.read_csv("E:\\python\\data.csv", usecols=[
                   0, 1], names=["harry", "har"])


print(file)
print(file.head(2))
print(file.tail(2))
print(file.isnull())
print(file.dropna(axis=1))
print(file.fillna(0))
print(file.fillna({"harry": 0, "har": 0}))


# fillna()
# replaces missing (NaN) values with specific values or methods like forward/backward fill.

# df.fillna(value=0)                         Replace all NaN with 0
# df.fillna(method='ffill')                  Forward fill previous values
# df.fillna(method='bfill')                  Backward fill next values
# df.fillna(axis=1)                          Fill NaN across columns (→)
# df.fillna(inplace=True)                    Modify original DataFrame directly
# df.fillna(limit=2)                         Fill only first 2 NaNs per column/row
# df.fillna(downcast='int')                  Downcast data type if possible


# dropna()
# removes rows or columns containing missing (NaN) values based on conditions.

# df.dropna(axis=0)                          Drop rows with NaN
# df.dropna(axis=1)                          Drop columns with NaN
# df.dropna(how='any')                       Drop if any NaN found (default)
# df.dropna(how='all')                       Drop only if all values are NaN
# df.dropna(thresh=2)                        Keep rows with at least 2 non-NaN values
# df.dropna(subset=['Age', 'Salary'])        Check NaN only in given columns
# df.dropna(inplace=True)                    Apply drop directly to original df
