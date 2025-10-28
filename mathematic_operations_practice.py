import numpy as np

# ADDITION
array_one = np.arange(1, 10).reshape(3, 3)
array_two = np.arange(10, 19).reshape(3, 3)
print(f'First Array: {array_one}')
print(f'Second Array: {array_two}')

added_array = array_one + array_two
print(f'Addition of both arrays are: {added_array}')
added_array = np.add(array_one, array_two)  # SECOND METHOD FOR ADDITION
print(f'Addition of both arrays from different method: {added_array}')

# SUBTRACTION
sub_array = array_one - array_two
print(f'Subtraction of both arrays are: {sub_array}')
sub_array = np.subtract(array_one, array_two)  # SECOND METHOD FOR SUBTRACTION
print(f'Subtraction of both arrays from different method: {sub_array}')

# MULTIPLICATION
mul_array = array_one * array_two
print(f'Multiplication of both arrays are: {mul_array}')
# SECOND METHOD FOR MULTIPLICATION
mul_array = np.multiply(array_one, array_two)
print(f'Multiplication of both arrays from different method: {mul_array}')

# DIVISION
div_array = array_one / array_two
print(f'Division of both arrays are: {div_array}')
div_array = np.divide(array_one, array_two)  # SECOND METHOD FOR MULTIPLICATION
print(f'Division of both arrays from different method: {div_array}')

# DOT PRODUCT
product_array = array_one @ array_two
print(f'Dot Product of both arrays are: {product_array}')
product_array = np.dot(array_one, array_two)  # SECOND METHOD FOR DOT PRODUCT
print(f'Dot Product of both arrays from different method: {product_array}')
product_array = array_one.dot(array_two)  # THIRD METHOD FOR DOT PRODUCT
print(f'Dot Product of both arrays from third method: {product_array}')

# FINDING MAXIMUM IN ARRAY
max_value = array_one.max()
max_values_colummn = array_one.max(axis=0)
max_values_row = array_one.max(axis=1)
print(f'Maximum element of array one is: {max_value}')
print(f'Maximum elements of column: {max_values_colummn}')
print(f'Maximum elements of row: {max_values_row}')
print(f'index of maximum element is: {array_one.argmax()}')

# FINDING MINIMUM IN ARRAY
min_value = array_one.min()
min_values_colummn = array_one.min(axis=0)
min_values_row = array_one.min(axis=1)
print(f'Minimum element of array one is: {min_value}')
print(f'Minimum elements of column: {min_values_colummn}')
print(f'Minimum elements of row: {min_values_row}')
print(f'index of minimimum element is: {array_one.argmin()}')


# FINDING MEAN(AVERAGE) OF THE ARRAY
avg_array = array_one.mean()
print(f'The average(mean) of array_one is: {avg_array}')

# STANDARD DAVIATION(USED TO FIND CONSISTENCY OF DATA, IF THE VALUE CLOSER TO MEAN THAN DATA IS CONSISTENT)
st_array = array_one.std()
print(f'Standard daviation of array_one is: {st_array}')

# LOG (tells you what power you need)
log_value = np.log2(20)
print(f'Log value: {log_value}')
