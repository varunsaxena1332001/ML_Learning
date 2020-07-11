import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# reading Data
data = pd.read_csv('headbrain.csv')
print(data.head())

# collecting X and Y
X=data['Head Size(cm^3)'].values
Y=data['Brain Weight(grams)'].values

# calculating coefficient

# mean X and Y
mean_x=np.mean(X)
mean_y=np.mean(Y)
print(mean_x)
print(mean_y)


# total number of values
n=len(X)

# using the formula to calculate b1 and b2
