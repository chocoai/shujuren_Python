import numpy as np
from keras.models import Sequential
from keras.layers import Dense

np.random.seed(7) # 可重复性实验
# 1 导入数据
dataset = np.loadtxt('data/pima-indians-diabetes.data.txt', delimiter=',')
X = dataset[:,0:8]
Y = dataset[:,8]
# 2 设计模型
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# 3 编译模型
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# 4 拟合模型
model.fit(X, Y, validation_split=0.33, epochs=150, batch_size=10)

