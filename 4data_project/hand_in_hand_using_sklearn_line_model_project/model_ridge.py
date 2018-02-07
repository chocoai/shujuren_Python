import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# 生成数据集
X, y, w = make_regression(n_samples=10, n_features=10,coef=True, random_state=1, bias=3.5)
print(X)
print(y)
print(w)

coefs = []
errors = []

alphas = np.logspace(-6, 6, 200)
print(alphas)

clf = Ridge()

# 根据不同alpha值训练Ridge模型
for a in alphas:
    # 设置模型的超参数值
    clf.set_params(alpha=a)
    clf.fit(X,y) # 训练模型
    coefs.append(clf.coef_) # 记录模型训练后的参数值
    errors.append(mean_squared_error(clf.coef_, w)) # 学习所得参数与期望参数的均方误差

print(coefs)
print(errors)



# 数据可视化
plt.figure(figsize=(20, 6))
plt.subplot(121)
ax = plt.gca()
ax.plot(alphas, coefs)
ax.set_xscale('log')
plt.xlabel('alpha')
plt.ylabel('weights')
plt.title('Ridge coefficients as a function of the regularization')
plt.axis('tight')
plt.subplot(122)
ax = plt.gca()
ax.plot(alphas, errors)
ax.set_xscale('log')
plt.xlabel('alpha')
plt.ylabel('error')
plt.title('Coefficient error as a function of the regularization')
plt.axis('tight')
plt.show()

# 结论：
# 10个权重对应10条直线

# 资料：
# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html
# https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_ridge_coeffs.py