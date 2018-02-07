"""
adaboost算法解决回归问题
"""

# 导入Python库
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor

# 数据集
rng = np.random.RandomState(20) # 可重复性实验
X = np.linspace(0, 6, 100)[:,np.newaxis]
y = np.sin(X).ravel() + np.sin(6 * X).ravel() + rng.normal(0, 0.1, X.shape[0])
# print(X)
# print(np.sin(X))
# print(np.sin(X).ravel())
# print(X.shape)
# print(y.shape)

# 训练回归模型
regr_1 = DecisionTreeRegressor(max_depth=4)
regr_2 = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4),n_estimators=300,random_state=rng)

regr_1.fit(X,y)
regr_2.fit(X,y)
y_1 = regr_1.predict(X)
y_2 = regr_2.predict(X)

# 数据结果可视化
plt.figure()
plt.scatter(X, y, c="k", label="training samples")
plt.plot(X, y_1, c="g", label="n_estimators=1", linewidth=2)
plt.plot(X, y_2, c="r", label="n_estimators=300", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Boosted Decision Tree Regression")
plt.legend()
plt.show()

# 结论：
# 期望函数的最佳逼近
# 集成的思想
# 资料：
# 1 http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html
# 2 https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_adaboost_regression.py

