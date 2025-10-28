import numpy as np

array = np.arange(2, 25, 2).reshape(3, 4)
print(f'Array: {array}')

print(f' Sliced array: {array[:, 2]}')
# print(f' Sliced array: {array[:, 0:2]}')
