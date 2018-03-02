import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris()

# 特征矩阵和目标变量
features_matrix = iris.data
target = iris.target
print(features_matrix.shape)
print(target.shape)

LR_model = LogisticRegression()
print(LR_model)

LR_model.fit(features_matrix, target)
print(LR_model)
# 测试数据集
test_pred = LR_model.predict([[5, 3, 5, 2.5]])
print(test_pred)

# 结论：
# 使用逻辑回归模型的默认参数

# 资料：
# http://blog.csdn.net/puqutogether/article/details/42971617