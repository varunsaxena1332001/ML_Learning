import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv('share.csv')
X = data['Head Size(cm^3)'].values
Y = data['Brain weight(grams)'].values
m = len(X)
X = X.reshape((m, 1))
reg = LinearRegression()
reg = reg.fit(X, Y)
print(reg.intercept_)
print(reg.coef_)
y_pred = reg.predict(X)
print(y_pred)

r2 = reg.score(X, Y)
print(r2)
mse = mean_squared_error(Y, y_pred)
rmse = np.sqrt(mse)
print(rmse)
