# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# 数据导入
dataset = pd.read_csv('data/50_Startups.csv')
print(dataset.shape)
print(dataset.head())

X = dataset[['R&D Spend', 'Administration', 'Marketing Spend', 'State']]
y = dataset[['Profit']]
print(X.head())
print(y.head())

X1 = X.values
# # 类别变量重编码
labelencoder_X = LabelEncoder()
X1[:,3] = labelencoder_X.fit_transform(X1[:,3])
print(X1[:3,])
onehotencoder = OneHotEncoder(categorical_features=[3])
X2 = onehotencoder.fit_transform(X1).toarray()
print(X2[:3,])
#
# # 避免虚拟变量陷阱
X3 = X2[:,1:]
print(X3[:3,])

X_train, X_test, y_train, y_test = train_test_split(X3, y, test_size=0.2, random_state=0)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
# 模型构建
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print(y_pred)

import statsmodels.formula.api as sm
X_train = np.append(arr=np.ones((40, 1)), values=X_train, axis=1)
print(X_train.shape)
# 特征选择
X_opt = X_train[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog= y_train, exog= X_opt).fit()
a = regressor_OLS.summary()
print(a)

