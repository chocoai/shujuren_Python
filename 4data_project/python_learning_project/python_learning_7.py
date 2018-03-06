# 多重继承
class people:
    name=''
    age=0
    __weight=0
    def __init__(self, n, a, w):
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print("%s say: I %d " %(self.name, self.age))

# 单继承实例
class student(people):
    grade=''
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade=g
    def speak(self):
        print("%s say: I %d and %d grade" %(self.name, self.age, self.grade))


class speaker():
    topic=''
    name=''
    def __init__(self, n, t):
        self.name=n
        self.topic=t
    def speak(self):
        print("%s say: topic %s"%(self.name, self.topic))

# 多重继承
class sample(speaker, student):
    a=''
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self,n,t)

test=sample("数据人", 25, 80, 4, "Python")
test.speak()