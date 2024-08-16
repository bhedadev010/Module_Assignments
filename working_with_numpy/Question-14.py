#Create a 2D NumPy array with shape (3, 4) initialized with ones,
# and then change its data type to int.

import numpy as np

array = np.ones((3,4)).astype('int64')

print(array)