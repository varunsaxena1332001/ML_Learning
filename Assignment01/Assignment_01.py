"""
Name = Varun Saxena
Program= calculation of brain weigth on basis of the size of head
Branch=Btech 3rd year
course=cse
Section =A
Rollno.=60
University RollNo.=181500783

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# reading Data
data = pd.read_csv('headbrain.csv')
print(data.head())

# collecting X and Y
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values

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

plt.xlabel('Head Size(cm^3)')
plt.ylabel('Brain Weight(grams)')
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

print("*" * 20)
x_particular = int(input('Enter a value of head size : '))
cal = b0 + b1 * x_particular
print("values of head size : ", x_particular)
print("calculated value of brain weight : ", cal)
