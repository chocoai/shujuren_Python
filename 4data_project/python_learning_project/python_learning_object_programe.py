#-*- coding:utf-8 -*-
# 程式设计思想
# 面向过程程式设计 一系列命令集合
# std1={'name':'A1', 'score':60}
# std2={'name':'A2', 'score':80}
# def print_score(std):
#     print('%s:%s' %(std['name'], std['score']))
# print(print_score(std1))
# print(print_score(std2))
# 面向对象程式设计 一系列对象集合
# class Student(object):
#     def __init__(self, name, score):
#         self.name=name
#         self.score=score
#     def print_score(self):
#         print('%s:%s' %(self.name, self.score))
#
# A1=Student('A1', 60)
# A2=Student('A2', 80)
# A1.print_score()
# A2.print_score()

#类和对象
# class Student(object):
#     def __init__(self, name, score):
#         self.name=name
#         self.score=score
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
# A1=Student('A1', 70)
# print(A1.name,A1.get_grade())
# A2=Student('A2', 80)
# print(A2.name, A2.get_grade())
#访问限制
# class Student(object):
#     def __init__(self, name, score):
#         self.__name=name
#         self.__score=score
#     def get_name(self):
#         return self.__name
#     def get_score(self):
#         return self.__score
#     def set_name(self, score):
#         if 0 <= score <= 100:
#             self.__score=score
#         else:
#             raise ValueError('bad score')
#
# A1=Student('A1', 80)
# print(A1.get_name())
# print(A1.get_score())
# 继承和多态
# class Animal(object):
#     def run(self):
#         print('Animal is running ....')
# class Dog(Animal):
#     def eat(self):
#         print('Eating meat ....')
#     def run(self):
#         print('Dog is running ....')
# class Cat(Animal):
#     pass
# dog=Dog()
# dog.run()
# dog.eat()
# cat=Cat()
# cat.run()
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
# run_twice(Animal())
# run_twice(Dog())

# 多态操作
# 方法覆盖

# 获取对象的信息
print(type(123))
print(type('123'))
print(type(None))
print(type(abs))
# 面向对象高级编程

#面型对象
#类的操作
class MyClass:
    """一个类实例"""
    i=12345
    def f(self):
        return "Hello world"

# 实例化类
x = MyClass()
# 访问类的属性和方法
print("MyClass类的属性i为：", x.i)
print("MyClass类的方法f输出为：", x.f())

class Complex:
    def __init__(self, realpart, imagepart):
        self.r = realpart
        self.i = imagepart

x=Complex(3.0, -4.5)
print(x.r, x.i)


class People:
    name = ''
    age = 0
    # 私有属性
    __weight = 0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s说: 我%d岁"%(self.name, self.age))

#实例化类
p = People('数据人', 10, 30)
p.speak()

