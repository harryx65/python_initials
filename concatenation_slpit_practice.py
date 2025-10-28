import numpy as np

array_one = np.arange(1, 17).reshape(4, 4)
array_two = np.arange(17, 33).reshape(4, 4)
array_three = np.arange(33, 49).reshape(4, 4)
array_four = np.arange(4, 15)


conc_array = np.concatenate((array_one, array_two))
conc_array = np.concatenate((array_one, array_two), axis=1)
conc_array = np.concatenate((array_one, array_two, array_three))
# print(conc_array)

hstack_array = np.hstack((array_one, array_two, array_three))
# print(hstack_array)

vstack_array = np.vstack((array_one, array_two, array_three))
# print(vstack_array)

split_array = np.split(array_one, 2)
split_array = np.split(array_one, 4, axis=1)
# print(array_one)
print(split_array)
oned_split_array = np.split(array_four, [3, 4, 8])
# print(oned_split_array)
