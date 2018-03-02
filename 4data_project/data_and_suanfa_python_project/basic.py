isMLGeek = True

if isMLGeek:
    print('推荐"数据-算法-Python"')

# Python数据类型
# 6 种
# 数字
# 布尔值
# 字符串
# 元祖
# 列表
# 字典

# Python数据运算
# 算术运算
# 比较运算
# 赋值运算
var1 = (1, 'hello', 0.4)
print(var1)
# 逻辑运算
# 成员运算
l = [1, 'abc', 0.4]
t = (1, 'abc', 0.4)
d = {1:'1', 'abc':0.1, 0.4:80}
print(1 in l)
print(1 in t)
print(1 in d) # 字典判断某个键是否存在

# Python流程控制
# 顺序执行
# 选择执行
# 重复执行

# 选址执行
b=True
if b:
    print("True")
else:
    print("False")

c=False
d=True
if c:
    print("True")
elif d:
    print("True")
else:
    print("False")

# 重复执行
dic1={'a':1, 'b':2, 'c':3}
for k in dic1:
    print(k,":",dic1[k])

# Python函数（模块）设计
def foo(x):
    return x ** 2
print(foo(8.0))

# Python编程库或者包的导入
import math
print(math.exp(2)) # 计算自然指数
from math import exp
print(exp(2))
from math import exp as ep
print(ep(2))

# Python基础综合应用
import pandas as pd
# 数据读入
df_train=pd.read_csv("Datasets/Breast-Cancer/breast-cancer-train.csv")
print(df_train.shape)
print(df_train.columns)
df_test=pd.read_csv("Datasets/Breast-Cancer/breast-cancer-test.csv")
print(df_test.shape)

# Pandas的datafram进行【行选择】
# 1）切片处理
print(df_train[:3])
# 2）loc[]方法按着指定索引选择一行或多行
print(df_train.loc[1:3])
print(df_train.loc[[1,3]])
# 3）iloc[]方法按着指定位置选择一行或多行
print(df_train.iloc[1:3])
print(df_train.iloc[[1,3]])

# pandas的dataframe进行【列选择】
# 根据列名选择
print(df_train["Cell Size"])
print(df_train[["Clump Thickness", "Cell Size"]])

# 构建测试集的正负分类样本
df_test_negative=df_test.loc[df_test["Type"]==0][["Clump Thickness", "Cell Size"]]
df_test_positive=df_test.loc[df_test["Type"]==1][["Clump Thickness", "Cell Size"]]
print(df_test_negative.shape)
print(df_test_positive.shape)

# 数据可视化
# 利用matplotlib包
import matplotlib.pyplot as plt
# plt.scatter(df_test_negative["Clump Thickness"], df_test_negative["Cell Size"], marker="o", s=200, c="red")
# plt.scatter(df_test_positive["Clump Thickness"], df_test_positive["Cell Size"], marker="x", s=150, c="black")
# plt.xlabel("Clump Thickness")
# plt.ylabel("Cell Size")
# plt.show()

# 数值化计算
# import numpy as np
# intercept=np.random.random([1])
# coef=np.random.random([2])
# print(intercept)
# print(coef)
# lx=np.arange(0, 12)
# ly=(-intercept - coef[0]*lx)/coef[1]
# plt.plot(lx, ly, c="yellow") # 绘制一条随机直线
# plt.show()

# 机器学习模型
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(df_train[["Clump Thickness", "Cell Size"]], df_train["Type"])
lr_test_score=lr.score(df_test[["Clump Thickness", "Cell Size"]], df_test["Type"])
print("测试数据集准确度：",lr_test_score)

print(lr.intercept_)
print(lr.coef_)
print(lr.coef_[0,:])

# 总结：






