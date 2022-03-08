# class Person:
#     pass
# p = Person()    # p是Person的对象
# print(p)


# 类的方法需要有一个self参数，Pycharm自动为你加上
# class Person:
#     def say_hello(self):
#         print('hello, world')
#
# p = Person()
# p.say_hello()
# Person().say_hello()


class Name:
    def __init__(self, name):
        self.name = name
        # __init__ 用来初始化对象

    def say_hello(self):
        print('my name is', self.name)
    # self.name 表明这个变量是类的一部分

p = Name('Zhu Xueteng')
p.say_hello()
print(p.name)   # not p.self.name





