#Python3基础知识
#-*- coding:utf-8 -*-

# list的遍历
# project_list = ["广州正佳广场", "广州天河城", "广州花城汇"]
#
# # 方法1
# print("遍历列表方法1")
# for i in project_list:
#     print("序号：%s 值: %s" % (project_list.index(i) + 1, i))
#
# # 方法2:
# print("遍历列表方法2")
# for i in range(len(project_list)):
#     print("序号:%s 值：%s" %(i + 1, project_list[i]))
#
# # 方法3
# print("遍历列表方法3")
# for i, var in enumerate(project_list):
#     print("序号:%s 值：%s" %(i + 1, var))
#
# for i in range(10):
#     print(i)
#
# for i in range(10, 12):
#     print(i)

# python基础
#1 数据类型和变量
#2 字符串和编码
#3 使用list和tuple
#4 条件判断
#5 循环
# names=['A', 'B', 'C']
# for name in names:
#     print(name)
#
# sum=0
# for x in range(1, 11):
#     sum=sum+x
# print(sum)
# print(range(5))
# print(list(range(5)))
# # -*- coding:utf-8 -*-
# sum1=0
# for x in range(101):
#     sum1=sum1+x
# print(sum1)
#
# #1到100所有奇数之和
# sum2=0
# n=99
# while n > 0:
#     sum2=sum2+n
#     n=n-2
# print(sum2)
#
# #1到100所有偶数之和
# sum3=0
# n=100
# while n > 0:
#     sum3=sum3+n
#     n-=2
# print(sum3)
#
# # 循环中的break和continue
# n=1
# while n<=100:
#     if n>10:
#         break
#     print(n)
#     n=n+1
# print("End")
#
# n=0
# while n<10:
#     n=n+1
#     if n%2 == 0:
#         continue
#     print(n)
#6 dict和set
# dict
# d={'A':85,'B':70,'C':100}
# print(d)
# print(d['A'])
# d['D']=90
# print(d)
# print('A' in d)
# print('E' in d)
# print(d.get('A'))
# print(d.get('E'))
# d.pop('D')
# print(d)
# # set
# s=set([1,2,3])
# print(s)
# s.add(4)
# print(s)
# s.add(4)
# print(s)
# s.remove(4)
# print(s)
#
# s1=set([1,2,3])
# s2=set([2,3,4])
# print(s1)
# print(s2)
# print(s1&s2)
# print(s1|s2)

#7 函数
# print(abs(-100))
# # print(abs(1, 2))
# print(max(1,2))
# print(max(2, 3, 1, -6))
# print(int('123'))
# n1=255
# print(hex(n1))
# n2=1000
# print(hex(n2))
# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x
# print(my_abs(-100))
#
# # 自定义函数，返回多个值
# import math
# def move(x, y, step, angle=0):
#     nx=x+step*math.cos(angle)
#     ny=y+step*math.sin(angle)
#     return nx, ny
# x,y=move(100, 100, 60, math.pi/6)
# print(x,y)
# r=move(100, 100, 60, math.pi/6)
# print(r)
# 必选参数，默认参数，可变参数，关键字参数和命名参数
# 函数操作
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

# print(my_abs(1))
# print(my_abs(-1))
# print(my_abs(1, 2))
# print(my_abs("A"))

def my_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')

def hello():
    print("Hello world!")
print(hello())

# 高级特性
# 1 切片
# 2 迭代
# d={'a':1, 'b':2, 'c':3}
# print(d)
# for key in d:
#     print(key)
#     print(d[key])
# for value in d.values():
#     print(value)
# for k,v in d.items():
#     print(k, v)
#
# str='hello'
# for ch in str:
#     print(ch)
# from collections import Iterable
# print(isinstance('abc', Iterable))
# print(isinstance((1,2,3), Iterable))
# print(isinstance([1,2,3], Iterable))
# print(isinstance(123, Iterable))
#
# list1=['A','B','C']
# for i, value in enumerate(list1):
#     print(i,value)
# 3 列表生成式
# print(list(range(1, 11)))
# list1=[x*x for x in range(1, 11)]
# print(list1)
# list2=[x*x for x in range(1, 11) if x % 2 == 0]
# print(list2)
# list3=['World','IBM', 'Apple']
# print([x for x in list3])
# print([x.lower() for x in list3])
# list4=['World','IBM', 'Apple', 15]
# print([x.lower() for x in list4 if isinstance(x,str)])
# 4 生成器
# L=[x*x for x in range(10)]
# print(L)
# g=(x*x for x in range(10))
# print(g)
# print(next(g))
# for n in g:
#     print(n)
# 5 迭代器
# 函数式编程
def add(x, y, f):
    return f(x) + f(y)
print(add(-5, -6, abs))

# map/reduce编程
def f(x):
    return x*x
r=map(f,list(range(1,11)))
print(list(r))
r1=map(str,list(range(1,11)))
print(list(r1))
# reduce函数
from functools import reduce
def fn(x,y):
    return x*10 + y
print(reduce(fn, [1,3,5,7,9]))


