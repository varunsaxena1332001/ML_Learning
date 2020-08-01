import numpy as np

a = np.array([1, 2, 3])
b = np.array([0, 1, 0])
print("Original 1-d arrays")
print(a)
print(b)
r = np.inner(a, b)
print(r)
