# -*- coding: utf-8 -*-
"""REGLOG_Version 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MooBdAMZrHsL0YqRU7PN1RZVXQQbxYF-
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

file_path = '/content/Data Casa complète.xlsx'
df = pd.read_excel(file_path, index_col=[0], parse_dates =True,header = 3)

df.shape

df.head(10)

df.tail()

df.columns

df.info()

df.nunique().sort_values()

df.describe()

sns.pairplot(df)
plt.show()

plt.figure(figsize=(30,7))
df.boxplot()

sns.histplot(df['temperature_2m (°C)'])

sns.kdeplot(df['temperature_2m (°C)'], shade=True)

plt.figure(figsize=(14,7))
sns.lineplot(x="time", y="temperature_2m (°C)", data=df)

df.corr()

sns.heatmap(df.corr(),annot=True, fmt=".1f")

X = df[[col for col in df.columns if col != "temperature_2m (°C)"]]

y = df["temperature_2m (°C)"]

X.shape, y.shape

from sklearn.model_selection import train_test_split

X = df[[col for col in df.columns if col != "temperature_2m (°C)"]]
y = df['temperature_2m (°C)']

X.head()



X_train, X_test, y_train, y_test= train_test_split(X,y, test_size=0.3)

import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression

df['relativehumidity_2m (%)']=df['relativehumidity_2m (%)'].fillna(0)

df['dewpoint_2m (°C)']=df['dewpoint_2m (°C)'].fillna(0)

df['apparent_temperature (°C)']=df['apparent_temperature (°C)'].fillna(0)

df['surface_pressure (hPa)']=df['surface_pressure (hPa)'].fillna(0)

df['cloudcover (%)']=df['cloudcover (%)'].fillna(0)

df['shortwave_radiation (W/m²)']=df['shortwave_radiation (W/m²)'].fillna(0)

df['direct_radiation (W/m²)']=df['direct_radiation (W/m²)'].fillna(0)

df['diffuse_radiation (W/m²)']=df['diffuse_radiation (W/m²)'].fillna(0)

df['windspeed_100m (m/s)']=df['windspeed_100m (m/s)'].fillna(0)

df['winddirection_100m (°)']=df['winddirection_100m (°)'].fillna(0)

df['windgusts_10m (m/s)']=df['windgusts_10m (m/s)'].fillna(0)

df['soil_moisture_28_to_100cm (m³/m³)']=df['soil_moisture_28_to_100cm (m³/m³)'].fillna(0)

!pip install sklearn.ensemble.HistGradientBoostingClassifier
modele_logit = LogisticRegression(penalty='none',solver='newton-cg')
modele_logit.fit (X_train,y_train)

X_stat = sm.add_constant(X)
model = sm.Logit(y, X_stat)
result = model.fit()

result.summary()

!pip install sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn import linear_model
df.head()

x = df [[col for col in df.columns if col != "temperature_2m (°C)"]]
y = df['temperature_2m (°C)']

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 0)

modele_regLog = linear_model.LogisticRegression(random_state = 0,
solver = 'liblinear', multi_class = 'auto')

import numpy as np
df['temperature_2m (°C)'].replace([np.nan], df['temperature_2m (°C)'].mean(), inplace=True)
df.fillna(df.mean(), inplace=True)
modele_regLog.fit(x_train,y_train)

#modele_regLog.fit(x_train,y_train)
precision = modele_regLog.score(x_test,y_test)
print(precision*100)

df = modele_regLog.predict([[180,8.0,6.8]])
df[df[0]]