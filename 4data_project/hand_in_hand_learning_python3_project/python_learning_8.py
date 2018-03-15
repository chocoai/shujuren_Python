# 方法重写
class Parent:
    def myMethod(self):
        print("调用父类方法")

class Child(Parent):
    def myMethod(self):
        print("调用子类方法")

c = Child()
c.myMethod()
super(Child,c).myMethod()

# 资料：
# http://www.runoob.com/python3/python3-class.html
