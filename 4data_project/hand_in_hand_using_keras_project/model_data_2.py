import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# 数据导入
wines = pd.read_csv("data/wines.csv")

# 数据集目标变量
y = wines.quality
# 数据集特征矩阵
X = wines.drop('quality', axis=1)
# 特征矩阵标准化处理
X = StandardScaler().fit_transform(X)

# 定义神经网络结构
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import r2_score
# 模型初始化
model = Sequential()

# 添加输入层
# model.add(Dense(64, input_dim = 12, activation='relu'))
# model.add(Dense(1))

# from keras.optimizers import RMSprop
# rmsprop = RMSprop(lr=0.0001)
# model.compile(optimizer=rmsprop, loss='mse', metrics=['mae'])

# from keras.optimizers import SGD, RMSprop
# sgd=SGD(lr=0.1)
# model.compile(optimizer=sgd, loss='mse', metrics=['mae'])

# 设置交叉验证
from sklearn.model_selection import StratifiedKFold
seed = 7
np.random.seed(seed)
kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
for train, test in kfold.split(X,y):
    model = Sequential()
    model.add(Dense(64, input_dim=12, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    model.fit(X[train],y[train], epochs=10, verbose=1)
    mse_value, mae_value = model.evaluate(X[test], y[test], verbose=0)
    print(mse_value),
    print(mae_value)
    y_pred = model.predict(X[test])
    print(r2_score(y[test], y_pred))


#资料：
#https://www.datacamp.com/community/tutorials/deep-learning-python








