from numpy import linalg as LA
import numpy as np

a = np.array([[1, 0], [0, 1]])
print(a)
print(LA.det(a))  # similar ar np.linalg.det(a)
