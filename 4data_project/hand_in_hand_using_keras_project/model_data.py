import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


# 数据导入
wines = pd.read_csv("data/wines.csv")
print(wines.head())

# 数据集划分
from sklearn.model_selection import train_test_split
X = wines.ix[:,0:11]
y = np.ravel(wines.type)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
print(X_train.shape)
print(X_test.shape)

# 数据标准化处理
# 针对列的列操作，使其均值为0，标注差为1
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# 模型设计和构建
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
# 定义神经网络结构
model.add(Dense(12, activation='relu', input_shape=(11,)))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# 输出模型所定义的信息
# print(model.output_shape)
# print(model.summary())
# print(model.get_config())
# print(model.get_weights())

# 编译和拟合模型
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=20, batch_size=1, verbose=1)

# 模型应用
y_pred = model.predict(X_test)
print(np.round(y_pred[:5]))
print(y_test[:5])


# 模型结果评价
score = model.evaluate(X_test, y_test,verbose=1)
print(score)
# 或者
# 利用sklearn的评价体系
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, cohen_kappa_score
# 混淆矩阵
print(confusion_matrix(y_test, y_pred))
print(precision_score(y_test, y_pred))
print(recall_score(y_test, y_pred))
print(f1_score(y_test,y_pred))
print(cohen_kappa_score(y_test, y_pred))







