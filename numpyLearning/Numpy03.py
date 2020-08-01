"""Some Mathematical Operations on numpy array"""

import numpy as np

n1 = np.array([[4, 5, 6], [4, 5, 6]])
n2 = np.array([[1, 2, 3], [1, 2, 3]])

# multiplication of two array by their index numbers
# for example , [n1[0]*n2[0],n1[1]*n2[1],n1[2]*n2[2]]

print(n1 * n2)

# addition of two numpy arrays
print(n1 + n2)

# subtraction of two numpy arrays
print(n1 - n2)
