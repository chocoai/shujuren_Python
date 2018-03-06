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

