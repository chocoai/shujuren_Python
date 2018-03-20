# # 类的继承机制
#
# # 类定义
# class people:
#     name=''
#     age=0
#     __weight=0
#     def __init__(self, n, a, w):
#         self.name=n
#         self.age=a
#         self.__weight=w
#     def speak(self):
#         print("%s说:我%d岁" %(self.name, self.age))
#
# # 类单继承
# class student(people):
#     grade=''
#     def __init__(self, n, a, w, g):
#         people.__init__(self, n, a, w)
#         self.grade=g
#     # 覆盖父类的方法
#     def speak(self):
#         print("%s 说： 我 %d 岁， 读 %d 年级"%(self.name, self.age, self.grade))
#
# s = student("数据人", 10, 60, 3)
# s.speak()
# 三维数组编程二维数组
import numpy as np
a=np.reshape(np.arange(18),(3,3,2))
print(a)
a1=np.reshape(a,(-1,2))
print(a1)

