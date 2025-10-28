import numpy as np

# ARRANGE FUNCTION

# np.arange(start, end, step)
arange_array = np.arange(1, 9)
print(arange_array)

# PRINT EVEN VALUES
even_array = np.arange(0, 9, 2)
print(f'Even Array: {even_array}')

# RESHAPE FUNCTION FOR 2D
reshape_array = arange_array.reshape(2, 4)
print(f'2 by 4 reshaped array: {reshape_array}')

# RESHAPE FUNCTION FOR 3D
reshape_array3d = arange_array.reshape(2, 2, 2)
print(f'3D reshaped array: {reshape_array3d}')

# RAVEL FUNCTION TO CONVERT MULTI DIMENSIONAL ARRAY TO 1D
oned_array = reshape_array3d.ravel()
print(f'1D Array: {oned_array}')

# TRANSPOSE (WE CAN ALSO USE .T FOR TRANSPOST)
trasnposed_array = reshape_array.transpose()
print(f'Transpose array: {trasnposed_array}')
