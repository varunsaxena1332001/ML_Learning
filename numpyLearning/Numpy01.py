"""Some use of Numpy functions"""
# np.array function convert a simple array into numpy array
a = [1, 2, 3]
print(a)
print("data type of array", type(a))

import numpy as np

b = np.array(a)
print("numpy array", b)
print("type of array", type(b))
print("datatype of variable", b.dtype)

# to produce an array of particular range
# np.arange(initial_element,final + 1 element,difference b/w numbers)
d = np.arange(0, 5, 2)
print(d)

# "shape" is used to get shape of array
print(b.shape)

# change the shape of array
c = np.array([[1, 2, 3], [4, 5, 6]])
c = c.reshape(3, 2)
print(c.shape)
print(c)

# "ndim" is used to know the dimensions of  array
print(c.ndim)

'''np.zeros() is used to create an array of '0' number'''
zr = np.zeros([3, 4])  # np.zeros([rows,columns])
print(zr)

'''np.ones() is used to create an array of '1' number'''
on = np.ones([2, 2])  # np.ones([rows,columns])
print(on)

# to create an array of size(2,2) of number 4
print(on * 4)
