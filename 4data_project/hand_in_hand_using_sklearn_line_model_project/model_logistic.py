#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
逻辑回归算法
"""
# 导入相应库和模块
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import matplotlib.font_manager as fm
myfont = fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')

# 构建人工数据集
xmin, xmax = -5,5
n_samples = 100
np.random.seed(0) # 可重复性试验
X = np.random.normal(size=n_samples)
print(X)
print(np.mean(X))
print(np.std(X))

# 通过比较关系运算
# 给目标变量进行0-1化处理
y = (X > 0).astype(np.float)
print(y)
X[X > 0] *= 4
X += .3 * np.random.normal(size=n_samples)

# 特征矩阵表示
X = X[:,np.newaxis]

# 建立分类模型
clf = linear_model.LogisticRegression(C=1e5)
clf.fit(X, y)

# 绘制逻辑回归的结果
plt.figure(1, figsize=(4, 3))
plt.figure(1)
plt.clf()
plt.scatter(X.ravel(), y, color='black', zorder=20)

X_test = np.linspace(-5, 10, 300)
def model(x):
    return 1 / (1 + np.exp(-x))
loss = model(X_test * clf.coef_ + clf.intercept_).ravel()
plt.plot(X_test, loss, color='red', linewidth=3)

ols = linear_model.LinearRegression()
ols.fit(X, y)
plt.plot(X_test, ols.coef_ * X_test + ols.intercept_, linewidth=1)
plt.axhline(.5, color='.5')

plt.ylabel('y')
plt.xlabel('X')
plt.xticks(range(-5, 10))
plt.yticks([0, 0.5, 1])
plt.ylim(-.25, 1.25)
plt.xlim(-4, 10)
plt.legend(('逻辑回归模型', '线性回归模型'),
           loc="lower right", fontsize='small', prop=myfont)
plt.show()

# 资料：
# https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_logistic.py
# https://www.zhihu.com/question/25404709