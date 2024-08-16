#Create a 1D NumPy array with shape (10,1) containing numbers
# from 100 to 109, and change its data type to float.

import numpy as np

array = np.arange(100,110).reshape((10,1)).astype('float64')

print(array)