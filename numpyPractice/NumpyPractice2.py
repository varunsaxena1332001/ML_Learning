# multiplication of outer matrices
import numpy as np

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
c = np.outer(matrix1, matrix2)
print(c)
