# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/genar/OneDrive/Área de Trabalho/Aurora Project/us-counties.csv', engine='python')

df0 = df[(df["county"] == 'Alachua') & (df["state"] == 'Florida')]

import datetime as dt
df0['date'] = pd.to_datetime(df0['date'])
df0['date'] = df0['date'].map(dt.datetime.toordinal)

X = df0['date'].values.reshape(-1, 1)
y = df0['cases'].values

#Regressão linear
from sklearn import linear_model
regressor1 = LinearRegression()
regressor1.fit(X, y)
score1 = regressor1.score(X, y)

fig, ax = plt.subplots(figsize=(10, 10))

ax.scatter(X, y, color='purple')
plt.plot(X, regressor1.predict(X), color = 'red')
ax.set(xlabel="Date",
       ylabel="Cases",
       title="Linear Regression for Daily Total Cases in Alachua County")

plt.show()

#Regressão polinomal
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree = 3)
X_poly = poly.fit_transform(X)

regressor2 = LinearRegression()
regressor2.fit(X_poly, y)
score2 = regressor2.score(X_poly, y)

import matplotlib.ticker as ticker

fig, ax = plt.subplots(figsize=(10, 10))

ax.scatter(X, y, color='purple')
plt.plot(X, regressor2.predict(poly.fit_transform(X)), color = 'red')
ax.set(xlabel="Date",
       ylabel="Cases",
       title="Polinomial Regression for Daily Total Cases in Alachua County")

plt.show()