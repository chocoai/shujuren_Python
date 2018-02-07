"""
lasso和elasticnet算法
"""

# 导入Python库
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# 数据集生成
np.random.seed(42)
n_samples, n_features = 50, 200
X = np.random.randn(n_samples, n_features)
coef = 3*np.random.randn(n_features)
inds = np.arange(n_features)
print(inds)
np.random.shuffle(inds)
print(inds)
coef[inds[10:]] = 0
y = np.dot(X, coef)
print(y)
# 添加噪声
y += 0.01 * np.random.normal(size=n_samples)
print(y)

# 数据集分割
X_train, y_train = X[:n_samples//2], y[:n_samples//2]
X_test, y_test = X[n_samples//2:], y[n_samples//2:]

# Lasso模型
from sklearn.linear_model import Lasso
alpha = 0.1
lasso = Lasso(alpha=alpha)
y_pred_lasso = lasso.fit(X_train, y_train).predict(X_test)
r2_score_lasso = r2_score(y_test, y_pred_lasso)
print(lasso)
print('测试数据集的R平方: %f' % r2_score_lasso)

# ElasticNet算法
from sklearn.linear_model import ElasticNet
enet = ElasticNet(alpha=alpha, l1_ratio=0.7)
y_pred_enet = enet.fit(X_train, y_train).predict(X_test)
r2_score_enet = r2_score(y_test, y_pred_enet)
print(enet)
print('测试数据集的R平方：%f' % r2_score_enet)

# 模型拟合数据可视化
# print(X_train.shape)
# print(enet.coef_)
plt.plot(enet.coef_, color='lightgreen', linewidth=2,
         label='Elastic net coefficients')
plt.plot(lasso.coef_, color='gold', linewidth=2,
         label='Lasso coefficients')
plt.plot(coef, '--', color='navy', label='original coefficients')
plt.legend(loc='best')
plt.title("Lasso R^2: %f, Elastic Net R^2: %f"
          % (r2_score_lasso, r2_score_enet))
plt.show()

# 资料：
# 1 http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html
# 2 https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_lasso_and_elasticnet.py


