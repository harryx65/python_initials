import numpy as np
import pandas as pd

df = pd.DataFrame({"a": [0, 1, 2, np.nan, 6, 7], "b": [
                  8, 9, np.nan, np.nan, 12, 13]})

df = df.interpolate()
print(df)


# df.interpolate()                                   Fill NaN values using linear interpolation along each column (default)
# df.interpolate(method='linear')                    Default linear interpolation between values
# df.interpolate(method='time')                      Fill missing values based on datetime index
# df.interpolate(method='polynomial', order=2)       Use polynomial interpolation of given order
# df.interpolate(axis=0)                             Interpolate column-wise (default)
# df.interpolate(axis=1)                             Interpolate row-wise
# df.interpolate(limit=1)                            Fill at most 1 consecutive NaN
# df.interpolate(limit_direction='forward')          Fill only in the forward direction
# df.interpolate(limit_direction='backward')         Fill only in the backward direction
# df.interpolate(limit_direction='both')             Fill in both directions
# df.interpolate(inplace=True)                       Apply interpolation directly to the original DataFrame
# df.interpolate(limit_area='inside')                Fill NaNs only bounded by valid values (not at ends)
# df.interpolate(limit_area='outside')               Fill NaNs at the start or end only
# df.interpolate(order=2)                            Degree of polynomial when using polynomial/spline method
# df.interpolate(downcast='infer')                   Convert result dtype if possible (e.g., float → int)
