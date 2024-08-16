#Create a 3D NumPy array with dimensions 2x3x4 containing random integers between 0 and 9.

import numpy as np

array = np.random.randint(0,10, size=(2,3,4))

print(array)