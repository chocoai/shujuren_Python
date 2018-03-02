import numpy as np
import pandas as pd

# 肿瘤识别问题
# 数据读入
# 创建列名
column_names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']
print(column_names)
print(len(column_names))
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data', names = column_names )
print(data.shape)
# 数据处理
data1=data.replace(to_replace="?", value=np.nan)
# 删除有缺失值的数据（只有有一个维度有缺失值）
data2=data1.dropna(how="any")
print(data2.shape)

# 数据集分割：训练集和测试集
# 训练集选择75%，测试集选择25%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(data2[column_names[1:10]], data2[column_names[10]], test_size=0.25, random_state=33)
# 训练样本和测试样本
print(y_train.value_counts())
print(y_test.value_counts())

# 分类模型
# 逻辑回归分类模型
# 随机梯度分类模型
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier

# 数据的标准化处理
# 每个维度的特征数据方差为1，均值为0
ss=StandardScaler()
X_train1=ss.fit_transform(X_train)
X_test1=ss.transform(X_test)
print(X_train1.shape)
print(X_test1.shape)

# 训练逻辑回归模型
lr=LogisticRegression()
lr.fit(X_train1, y_train)
lr_y_predict=lr.predict(X_test1)

# 训练SGD分类器模型
sgdc=SGDClassifier()
sgdc.fit(X_train1, y_train)
sgdc_y_predict=sgdc.predict(X_test1)

# 模型性能分析
from sklearn.metrics import classification_report
#逻辑回归模型自带评分函数，计算模型准确度
print("LR准确度：", lr.score(X_test1,y_test))
# 利用分类性能报告函数
print(classification_report(y_test, lr_y_predict, target_names=["Benign", "Malignant"]))
#SGD分类器的自带评分函数，计算模型准确度
print("SGD准确度：", sgdc.score(X_test1, y_test))
print(classification_report(y_test, sgdc_y_predict, target_names=["Benign", "Malignant"]))

# 结论：
# 基准算法：线性分类器
# 逻辑回归或者随机梯度分类器
# 数值解析求优化
# 梯度下降求优化，适合于大数据处理（10万量级以上数据）






