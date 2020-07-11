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