import numpy as np

# 1-DIMENSIONAL ARRAY

array_oned = np.array(["Haris", "Harry", "Me"])
print(f'Array elements are: {array_oned}')
print(f'Array Shape: {array_oned.shape}')
print(f'Array Size: {array_oned.size}')
print(f'Array element on index 2: {array_oned[2]}')
print(f'Array Dimension {array_oned.ndim}')
print(f'Array Type {array_oned.dtype}')


# 2-DIMENSIONAL ARRAY

array_twod = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
print(f'2 Dimesional array elements are: {array_twod}')
print(f'2 Dimensional array shaped: {array_twod.shape}')
print(f'2 Dimensional array size: {array_twod.size}')
print(f'2 Dimensional array dimesion: {array_twod.ndim}')
print(f'2 Dimensional array element at index: {array_twod[1, 1]}')
print(f'2 Dimensional array tyoe: {array_twod.dtype}')


# 3-DIMENSIONAL ARRAY

array_threed = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ],
    [
        [9, 0, 5, 6],
        [4, 7, 8, 9]
    ]
])
print(f'3 Dimensional array elements are: {array_threed}')
print(f'3 Dimensional array shape: {array_threed.shape}')
print(f'3 Dimensional array size: {array_threed.size}')
print(f'3 Dimensional array dimension {array_threed.ndim}')
print(f'3 Dimensional array element at index: {array_threed[1, 0, 2]}')
print(f'2 Dimensional array type: {array_twod.dtype}')

# ZERO'S ARRAY

array_zero = np.zeros((3, 3), dtype=int)
print(f'Zero array: {array_zero}')
print(f'Array Type: {array_zero.dtype}')
