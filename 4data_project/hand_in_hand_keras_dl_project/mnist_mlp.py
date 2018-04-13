# -*- coding:utf-8 -*-

import keras
from keras.datasets import mnist
from keras.layers import Dense
from keras.layers import Dropout
from keras.optimizers import RMSprop

batch_size = 128
num_classes = 10
