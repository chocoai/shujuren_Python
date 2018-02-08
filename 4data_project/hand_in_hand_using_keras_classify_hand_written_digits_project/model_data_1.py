from keras.datasets import mnist

# 数据导入

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 数据可视化
digit = train_images[4]
import matplotlib.pyplot as plt
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()


# 数据查看
# 训练数据集：用来学习最逼近数据洞见的模型
print(train_images.shape)
print(len(train_images))
print(train_labels)
# 测试数据集：用来测试和应用模型的，测试模型可以做评价，应用模型可以解决估算和标注等问题
print(test_images.shape)
print(len(test_images))
print(test_labels)
# 机器学习工作流：训练-预测-验证-应用
# 利用训练数据集训练模型
# from keras.models import Sequential
# from keras.layers import Dense
#
# # 设计和定义神经网络结构
# network = Sequential()
# network.add(Dense(512, activation='relu', input_shape=(28 * 28, )))
# network.add(Dense(10, activation='softmax'))
#
# # 编译阶段
# network.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
#
# # 数据集预处理
# train_images = train_images.reshape((60000, 28 * 28))
# train_images = train_images.astype('float32') / 255
# test_images = test_images.reshape((10000, 28 * 28))
# test_images = test_images.astype('float32') / 255
# from keras.utils import to_categorical
# train_labels = to_categorical(train_labels)
# test_labels = to_categorical(test_labels)
#
# # 训练模型
# network.fit(train_images, train_labels, epochs=1, batch_size=1204)
#
# # 测试数据集上评价网络
# test_loss, test_acc = network.evaluate(test_images, test_labels)
# print('test_acc:', test_acc)


