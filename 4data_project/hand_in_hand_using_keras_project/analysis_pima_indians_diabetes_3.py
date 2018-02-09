import numpy
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

seed = 7
np.random.seed(seed)

# 1 数据导入
dataset = np.loadtxt('data/pima-indians-diabetes.data.txt', delimiter=',')
X = dataset[:,0:8]
Y = dataset[:,8]
# 数据集分割
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=seed)

# 2 创建模型
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 3 编译模型
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 4 拟合模型
model.fit(X_train, y_train, validation_data=(X_test,y_test), epochs=150, batch_size=10)