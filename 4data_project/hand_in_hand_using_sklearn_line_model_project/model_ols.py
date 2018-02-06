#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
线性回归算法
"""
# 导入相应库和模块
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# 加载糖尿病数据集
diabetes = datasets.load_diabetes()
print(diabetes.data[[1,2]])

# 选择数据集中的某一列
diabetes_X = diabetes.data[:, np.newaxis, 2]
print(diabetes_X[[1,2]])
print(diabetes_X.shape)
# 数据集划分
# 训练集
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
print(diabetes_X_train.shape)
print(diabetes_X_test.shape)
# 测试集
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# 创建线性回归模型
regr = linear_model.LinearRegression()
# 训练数据集训练模型
regr.fit(diabetes_X_train, diabetes_y_train)
# 测试数据集上做预测
diabetes_y_pred = regr.predict(diabetes_X_test)
# 回归模型的系数
print('一元线性回归模型的系数:\n', regr.coef_)
# 回归模型的偏置
print('一元线性回归模型的偏置:\n', regr.intercept_)
# 度量指标：均方误差
print('一元线性回归模型的均方误差:%.2f' % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# 模型的解释度
print('一元线性回归模型的的R平方值:%.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

#数据可视化
plt.scatter(diabetes_X_test, diabetes_y_test, color = 'black')
plt.scatter(diabetes_X_test, diabetes_y_pred, color = 'blue', linewidths=3)
plt.xticks(())
plt.yticks(())
plt.show()

# 资料：
# https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_ols.py

