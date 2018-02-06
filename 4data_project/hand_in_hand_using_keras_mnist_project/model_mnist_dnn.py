'''Trains a simple deep NN on the MNIST dataset.
Gets to 98.40% test accuracy after 20 epochs
(there is *a lot* of margin for parameter tuning).
2 seconds per epoch on a K520 GPU.
'''

'''
MNIS数据集训练一个简单的DNN

'''

from keras.datasets import mnist
from keras.datasets import imdb
from keras.datasets import cifar
from keras.datasets import
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop

batch_size = 128
num_classes = 10
epochs = 20

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print(x_train.shape[0],'训练样本数')
print(x_test.shape[0], '测试样本数')

# 把类被向量转换为二进制类别矩阵
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

# 定义神经网络结构
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))
print(model.summary())

# 模型编译和拟合
model.compile(loss="categorical_crossentropy", optimizer=RMSprop(), metrics=['accuracy'])
history = model.fit(
    x_train,
    y_train,
    batch_size=batch_size,
    epochs=2,
    verbose=1,
    validation_data=(x_test,y_test)
)
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy', score[1])

# 资料：
# https://github.com/keras-team/keras/blob/master/examples/mnist_mlp.py