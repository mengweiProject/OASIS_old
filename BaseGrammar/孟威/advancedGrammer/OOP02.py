"""
super（）用法
"""


# class A:
#     def __init__(self, age):
#         self.age = age
#
#     def say(self, name):
#         print(f'{name} say hello...')
#
#
# class B(A):
#     def __init__(self, age, height):
#         super(B, self).__init__(age)
#         self.height = height
#
#
#     def say(self, name, target):
#         super(B, self).say(name)
#         print(f'{name} say hello to {target}')
#
#
#
# if __name__ == '__main__':
#     # a = A()
#     # a.say('xiaohuang', 'xiaolv')
#     b = B()
#     b.say('xiaohuang', 'xiaolv')

# 16. 设置只读属性的两种方案
# 16.1 @property装饰器
# 隐式继承object，新式类
# class Person:
#     def __init__(self, name):
#         # 先设置一个私有属性
#         self.__name = name
#
#     @property
#     def name(self):
#         """ property装饰器，使得一个方法可以像一个属性一样被访问 """
#         return self.__name
#
#     @name.setter
#     def name(self, n_name):
#         self.__name = n_name
#
# p = Person('小红')
# print(p.name)
# # p.name = '小绿'
# # 名称重整机制：{'_Person__name': '小红'}
# print(p.__dict__)
# p._Person__name = '小紫'
# print(p.name)

# 16.2 __setattr__（）方法
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __setattr__(self, key, value):
#         print(key, value)
#         self.__dict__[key] = value
#
#
# p = Person('xiaohong')
# print(p.name)

# 17. 比较对象的大小
# class A:
#     def __init__(self, age):
#         self.age = age
#     def __lt__(self, other):
#         print(self)
#         print(other)
#         return self.age < other.age
#
#
#
# a = A(22)
# b = A(18)
# print(a > b)

# 17.2 比较对象的大小
# 当我们实现了__lt__（）和__eq__（）方法后，只能使用小于号比较，或者等于号比较，并不能直接使用小于等于这种叠加操作
# 那么要如何使用叠加呢
# import functools
#
# @functools.total_ordering
# class Person:
#     def __lt__(self, other):
#         print('lt')
#
#     def __eq__(self, other):
#         print('eq')
#
# p1 = Person()
# p2 = Person()
# print(p1.__dict__)
# print(p1 <= p2)


# 25. 对象的遍历
# l = list()

# class List:
#     def __init__(self):
#         pass
#
#     def __getitem__(self, item):
#         print(self, item)
#         return item
#
#
# l = List()
# for i in l:
#     print(i)

# 26. __iter__（）方法，迭代器
# class MyList:
#     # def __init__(self, l_list):
#     #     self.__l_list = l_list
#
#     # def __getitem__(self, item):
#     #     return self
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         print('next')
#         return 2




# # l = MyList([1, 2, 3, 4, 5])
# l = MyList()
# for item in l:
#     print(item)



# class Person:
#     def __init__(self):
#         self.age = 1
#
#     def __iter__(self):
#         self.age = 1
#         return self
#
#     def __next__(self):
#         self.age += 1
#         if self.age >= 120:
#             raise StopIteration('stop')
#         return self.age
#
#
# p = Person()
# # from collections import Iterator
# #
# # print(isinstance(p, Iterator))
#
# for i in p:
#     print(i)
#
# for i in p:
#     print(i)

# 29. 描述器的使用
# class Person:
#     def __init__(self):
#         self.__age = 18
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, value):
#         if self.__age < 0:
#             print(f'年龄不合法')
#         else:
#             self.__age = value
#
#     def del_age(self):
#         del self.__age
#
#     age = property(get_age, set_age, del_age)
#
#
# p = Person()
# print(p.age)
# p.age = 19
# print(p.age)

# 30. 描述器的使用方法2

# class Age:
#     def __set__(self, instance, value):
#         print('set')
#
#     def __get__(self, instance, owner):
#         print('get')
#
#     def __delete__(self, instance):
#         print('delete')
#
# class Person:
#     age = Age()
#
#
# p = Person()
# print(p.age)
# p.age = 18
# del p.age


# 31. 描述器的数据存储
# class Age:
#     def __set__(self, instance, value):
#         # self.x = value
#         instance.x = value
#
#     def __get__(self, instance, owner):
#         # return self.x
#         return instance.x
#
#     def __delete__(self, instance):
#         print('delete')
#
#
# class Person:
#     age = Age()
#
#
# p1 = Person()
# p1.age = 10
# print(p1.age)
#
# p2 = Person()
# p2.age = 20
# print(p2.age)
# print(p1.age)



# 32. 类装饰器
#
# class Check:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         self.func(*args, **kwargs)
#
#
# @Check
# def fapengyouquan(name, content):
#     print(f'{name}发了一个朋友圈，内容是：{content}')
#
#
#
# fapengyouquan('小绿', '好一个凉爽的秋天!')


# 垃圾回收
# 33. 查看对象的内存地址
# n = 3
# print(id(n))
# print(n.__class__)
# print(n.__str__())
# print(n.__class__)
# print(id(2))
# n = 2
# print(id(n))


# l1 = [1, 2, 3, [4, 5]]
#
# l2 = l1
# print(l1)
# print(l2)
# l1[3][0] = 444
# print(l1)
# print(l2)

# l2 = l1.copy()
# print(l1)
# print(l2)
# l1[0] = 111
# print(l1)
# print(l2)



# 45. 多继承的覆盖
# class D:
#     def run(self):
#         print('DDD')

# class C(D):
#     def run(self):
#         print('CCC')
# class B(D):
#     # def run(self):
#     #     print('DDD')
#     pass
#
# class A(B, C):
#     # def run(self):
#     #     print('DDD')
#     pass
#
# a = A()
# a.run()

# 46. 多继承的覆盖
# class D:
#     def run(self):
#         print('DDD')
#
# class C(D):
#     def run(self):
#         print('CCC')
#         print(self)
#
#     @classmethod
#     def test(cls):
#         print(cls)
#
# class B(D):
#     # def run(self):
#     #     print('DDD')
#     pass
#
# class A(B, C):
#     # def run(self):
#     #     print('DDD')
#     pass
#
# a = A()
# a.run()
# a.test()

# 47. 抽象类和抽象方法
# import abc
#
# class Animal(object, metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def call(self):
#         pass
#
# # class Dog(Animal):
# #     def call(self):
# #         print('汪汪汪')
#
# a = Animal()
# a.call()


# 50. 面向的对象应用案例

import abc

class Animal(object, metaclass=abc.ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self}正在跑...')

    def sleep(self):
        print(f'{self}正在睡觉...')

    def eat(self):
        print(f'{self}正在吃饭...')

class Dog(Animal):
    def work(self):
        print(f'{self}正在看家...')

    def __str__(self):
        return f'名字为{self.name}年龄是{self.age}的小狗'


class Cat(Animal):

    def work(self):
        print(f'{self}正在捉老鼠...')

    def __str__(self):
        return f'名字为{self.name}年龄是{self.age}的小猫'

class Person(Animal):
    def __init__(self, name, age, pets):
        super().__init__(name, age)
        self.pets = pets

    def keep_pets(self):
        print(f'名字为{self.name}年龄是{self.age}的人正在养宠物...')
        for pet in self.pets:
            pet.eat()
            pet.run()
            pet.sleep()

    def let_pet_work(self):
        print(f'名字为{self.name}年龄是{self.age}的人正在让宠物工作...')
        for pet in self.pets:
            pet.work()

d = Dog('小黑', 4)
c = Cat('小红', 3.5)

p = Person('小明', 12, [d, c])
p.keep_pets()