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

# using the formula to calculate b0 and b1
numer=0
denom=0

for i in range(n):
    numer+=(X[i]-mean_x)*(Y[i]-mean_y)
    denom+=(X[i]-mean_x)**2
b1=numer/denom
b0=mean_y-(b1*mean_x)
