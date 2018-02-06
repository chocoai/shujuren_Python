# 导入所需库
import numpy as np
np.random.seed(123) # 可重复性实验
# keras的模型模块
from keras.models import Sequential
# keras的核心层模块
from keras.layers import Dense, Dropout, Activation, Flatten
# keras的CNN层模块
from keras.layers import MaxPooling2D
from keras.layers.convolutional import Conv2D
# 数据转化工具
from keras.utils import np_utils

# 数据加载
# mnist数据集
from keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)

# 数据可视化
# from matplotlib import pyplot as plt
# plt.imshow(X_train[0])

# 数据预处理
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

# 定义神经网络结构
model = Sequential()
# 输入层
model.add(Conv2D(32, 3, 3, activation='relu', input_shape=(28, 28, 1)))
model.add(Conv2D(32, 3, 3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))
print(model.output_shape)

# 模型编译
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
# 模型拟合
model.fit(X_train, Y_train,
          batch_size=32, epochs=10, verbose=1)

score = model.evaluate(X_test, Y_test, verbose=0)

# 资料：
# https://elitedatascience.com/keras-tutorial-deep-learning-in-python


