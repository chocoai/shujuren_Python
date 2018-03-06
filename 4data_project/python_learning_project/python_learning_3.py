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