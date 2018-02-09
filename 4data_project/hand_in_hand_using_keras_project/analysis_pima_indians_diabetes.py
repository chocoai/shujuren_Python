# keras建模的流程
# Load Data.
# Define Model.
# Compile Model.
# Fit Model.
# Evaluate Model.

import numpy as np
from keras.models import Sequential
from keras.layers import Dense

np.random.seed(7) # 可重复性实验
# 1 导入数据
dataset = np.loadtxt('data/pima-indians-diabetes.data.txt', delimiter=',')
X = dataset[:,0:8]
Y = dataset[:,8]

print(X.shape)
print(Y.shape)
print(X[0:6, 0:2])
print(Y[0:6,])

# 2 定义模型（设计神经网络结构）
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 3 编译模型
model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# 4 拟合模型
model.fit(
    X,
    Y,
    batch_size=10,
    epochs=150
)

# 5 评价模型
scores = model.evaluate(X,Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# 资料：
# https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/