"""
Name = Varun Saxena
Program=
Branch=Btech 3rd year
course=cse
Section =A
Rollno.=60
University RollNo.=181500783

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('share.csv')
print(data.head())
# data = data.replace('*', np.nan, inplace=True)
print(data.dtypes)
X = data['Age-Adjusted Death Rate']
Y = data['Lower 95% Confidence Interval for Death Rate']

X = X.replace('*', np.nan)
Y = Y.replace('*', np.nan)


X.fillna((X.median()), inplace=True)
Y.fillna((Y.median()), inplace=True)

X = X.astype('float64')
Y = Y.astype('float64')

# print(X)
# print(Y)

print(X.dtype)
print(Y.dtype)

# calculating coefficient

# mean X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)
print(mean_x)
print(mean_y)

# total number of values
n = len(X)

# using the formula to calculate b0 and b1
numer = 0
denom = 0

for i in range(n):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
b1 = numer / denom
b0 = mean_y - (b1 * mean_x)

# printing coefficient
print(b1)
print(b0)

max_x = np.max(X) + 100
min_x = np.min(X) + 100

# calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = b0 + b1 * x

# ploting line
plt.plot(x, y, color='#58b970', label='Regression Line')
# ploting Scatter Points
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')

plt.xlabel('Age-Adjusted Death Rate')
plt.ylabel('Lower 95% Confidence Interval for Death Rate')
plt.legend()
plt.show()

# calculating Root Mean Squares Error
rmse = 0
for i in range(n):
    y_pred = b0 + b1 * X[i]
    rmse += (Y[i] - y_pred) ** 2
rmse = np.sqrt(rmse / n)
print("RMSE")
print(rmse)
# calculating R2 Score
ss_tot = 0
ss_res = 0
for i in range(n):
    y_pred = b0 + b1 * X[i]
    ss_tot += (Y[i] - mean_y) ** 2
    ss_res += (Y[i] - y_pred) ** 2
r2 = 1 - (ss_res / ss_tot)
print("R2 Score")
print(r2)

