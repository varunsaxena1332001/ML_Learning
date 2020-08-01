# program to multiply two matrices
import numpy as np

matrix1 = np.array([[1, 0], [0, 1]])
matrix2 = np.array([[1, 2], [3, 4]])
c = np.dot(matrix1, matrix2)
print("Multiplication two matrices : ", c)
