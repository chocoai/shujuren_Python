import pandas as pd

# 读取white-wine数据
white = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=';')

# 读取read-wine数据
red = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';')

# 数据查看
print(white.shape)
print(red.shape)
# print(white.head())
# print(red.head())

# 数据探索
print(white.info())
print(red.info())

# 数据质量检查
# 1 数据类型是否正确
# 2 所有的行都获取了吗？
# 3 数据清理是，数据空值如何识别和处理
print(red.head())
print(red.tail())
print(red.sample(5))
print(red.describe())
print(pd.isnull(red))

# 数据可视化操作
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(1, 2)
# ax[0].hist(red.alcohol, 10, facecolor='red', alpha=0.5, label="Red wine")
# ax[1].hist(white.alcohol, 10, facecolor='white', ec="black", lw=0.5, alpha=0.5, label="White wine")
# #fig.subplots_adjust(left=0, right=1, bottom=0, top=0.5, hspace=0.05, wspace=1)
# ax[0].set_ylim([0, 1000])
# ax[0].set_xlabel("Alcohol in % Vol")
# ax[0].set_ylabel("Frequency")
# ax[1].set_xlabel("Alcohol in % Vol")
# ax[1].set_ylabel("Frequency")
#ax[0].legend(loc='best')
#ax[1].legend(loc='best')
# fig.suptitle("Distribution of Alcohol in % Vol")
# plt.show()

# 直方图分箱的值
# import numpy as np
# print(np.histogram(red.alcohol, bins=[7,8,9,10,11,12,13,14,15]))
# print(np.histogram(white.alcohol, bins=[7,8,9,10,11,12,13,14,15]))

# 两个变量的散点图
# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots(1, 2, figsize=(8, 4))
#
# ax[0].scatter(red['quality'], red["sulphates"], color="red")
# ax[1].scatter(white['quality'], white['sulphates'], color="white", edgecolors="black", lw=0.5)
#
# ax[0].set_title("Red Wine")
# ax[1].set_title("White Wine")
# ax[0].set_xlabel("Quality")
# ax[1].set_xlabel("Quality")
# ax[0].set_ylabel("Sulphates")
# ax[1].set_ylabel("Sulphates")
# ax[0].set_xlim([0,10])
# ax[1].set_xlim([0,10])
# ax[0].set_ylim([0,2.5])
# ax[1].set_ylim([0,2.5])
# fig.subplots_adjust(wspace=0.5)
# fig.suptitle("Wine Quality by Amount of Sulphates")
#
# plt.show()

# 数据可视化
# import numpy as np
# np.random.seed(570)
# # 数据集的label值
# redlabels = np.unique(red['quality'])
# whitelabels = np.unique(white['quality'])
#
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(1, 2, figsize=(8, 4))
# redcolors = np.random.rand(6, 4)
# print(redcolors)
# whitecolors = np.append(redcolors, np.random.rand(1, 4), axis=0)
# print(whitecolors)
# print(len(redcolors))
# for i in range(len(redcolors)):
#     redy = red['alcohol'][red.quality == redlabels[i]]
#     redx = red['volatile acidity'][red.quality == redlabels[i]]
#     ax[0].scatter(redx, redy, c=redcolors[i])
# for i in range(len(whitecolors)):
#     whitey = white['alcohol'][white.quality == whitelabels[i]]
#     whitex = white['volatile acidity'][white.quality == whitelabels[i]]
#     ax[1].scatter(whitex, whitey, c=whitecolors[i])
#
# ax[0].set_title("Red Wine")
# ax[1].set_title("White Wine")
# ax[0].set_xlim([0, 1.7])
# ax[1].set_xlim([0, 1.7])
# ax[0].set_ylim([5, 15.5])
# ax[1].set_ylim([5, 15.5])
# ax[0].set_xlabel("Volatile Acidity")
# ax[0].set_ylabel("Alcohol")
# ax[1].set_xlabel("Volatile Acidity")
# ax[1].set_ylabel("Alcohol")
# # ax[0].legend(redlabels, loc='best', bbox_to_anchor=(1.3, 1))
# ax[1].legend(whitelabels, loc='best', bbox_to_anchor=(1.3, 1))
# # fig.suptitle("Alcohol - Volatile Acidity")
# fig.subplots_adjust(top=0.85, wspace=0.7)
#
# plt.show()

# 数据预处理操作
# 添加类型变量
red['type'] = 1
white['type'] = 0
wines = red.append(white, ignore_index=True)

print(wines.shape)
print(wines.head())
print(wines.tail())

# 数据保存
wines.to_csv("data/wines.csv", index=False, encoding="utf-8")