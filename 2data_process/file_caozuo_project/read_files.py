# -*- coding:utf8 -*-
import codecs
import os

path = "data/" #文件夹目录
# 函数listdir罗列文件夹所有的文件
files= os.listdir(path) #得到文件夹下的所有文件名称
print(files)

s = []
for file in files: #遍历文件夹
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
          f = open(path+"/"+file, '', encoding="utf8") #打开文件
          iter_f = iter(f)#创建迭代器
          str = ""
          for line in iter_f: #遍历文件，一行行遍历，读取文本
              str = str + line
          s.append(str) #每个文件的文本存到list中
print(s) #打印结果

# 参考资料
# http://blog.csdn.net/kanon122500000/article/details/57111153
#