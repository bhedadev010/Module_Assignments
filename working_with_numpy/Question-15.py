# Create a 3D NumPy array with shape (2, 2, 3) initialized with specified numbers
# [[1, 2, 3], [4, 5, 6]], and [[7, 8, 9], [10, 11, 12]].

import numpy as np

array = np.arange(1,13).reshape((2,2,3))

print(array)