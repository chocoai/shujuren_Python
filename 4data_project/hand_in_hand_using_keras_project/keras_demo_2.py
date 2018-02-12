from keras.datasets import cifar10
import numpy as np

np.random.seed(10)

(x_img_train, y_label_train), (x_img_test, y_label_test) = cifar10.load_data()
print("train data:","images:",x_img_train.shape, "label:", y_label_train.shape)
print("test data:", "images:",x_img_test.shape, "label", y_label_test.shape)