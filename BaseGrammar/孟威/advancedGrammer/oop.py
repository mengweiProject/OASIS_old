'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/4/1 10:23 
'''

# class Animal:
#     pass
#
# class Person(Animal):
#     pass
#
# class Student(Person):
#     pass
#
#
# class A:
#     def __init__(self):
#         print('this is A')
#
#     def say(self):
#         print('say AAA')
#
#
# class B:
#     def __init__(self):
#         print('this is B')
#
#     def say(self):
#         print('say BBB')
#
#
# class C(A, B):
#     pass
#
#
#
# if __name__ == '__main__':
#     c = C()
#     print(c.say())
#     # s = Student()
#     # print(dir(s))
#     # print(Student.mro())

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def s_name(self, new_name):
#         self.new_name = new_name
#
#
# s = Student('xiaohong', 13)
# print(s.name)
# s.s_name('xiaohuang')
# print(s.new_name)


# class Person:
#     age = 18
#     name = 'xiaohuang'
#
# p = Person()
# print(p.name)
# p.name = 'xiaolv'
# print(p.name)
#
#
# q = Person()
# print(q.name)
#
# Person.name = 'xiaozi'
# print(q.name)
#
# o = Person()
# print(o.name)

# -------------面向对象--类属性--修改属性-------------

# class Person:
#     age = 18
#     name = 'xiaohuang'
#
#
# p = Person()
# Person.age = 28
# print(p.age)
# print(Person.age)


# a = 'abcaaa1#q34ehw45th4w5jsrtn'
# b = 'abcaaa1#q34ehw45th4w5jsrtn'
# print(a is b)


# class A:
#     age = 18
#     s1 = 'asdf'
#     s2 = 'ă'
#
#
# class B:
#     age = 18
#     s1 = 'asdf'
#     s2 = 'ă'


# print(A.age is B.age)
# print(A.s1 is B.s1)
# print(A.s2 is B.s2)


# for i in range(240, 260):
#     print(chr(i))

# print(ord('赵'))

# import pandas as pd
# data=['aa', 'aa', 'aa', 'bb', 'bb', 'bb', 'bb']
# num=[1,2,2,1,2,1,2]
# df1=pd.DataFrame({'name':data,'num':num})
# print(df1)
#
# # df1['mmm']=df1['num']
# df2=df1.groupby(['name'], as_index=False).sum()
# print(df2)


#
# a = '13453y6568678967'
# b = '13453y6568678967'
#
# print(a is b)



# 1. 类方法的调用
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def leifangfa(cls):
#         print('这是类方法')
#
# Person.leifangfa()
# p = Person('xiaohuang')
# p.leifangfa()


# 2. 静态方法及其调用
# class Person:
#     @staticmethod
#     def jingtai():
#         print('这是一个静态方法')
#
#
# Person.jingtai()
# p = Person()
# p.jingtai()



# 3. 三种方法访问两种属性的权限问题
# class Person:
#     age = 18
#
#     def __init__(self):
#         self.name = 'xiaohuang'
#         self.height = 188
#
#     def shilifangfa(self):
#         # 实例方法可以访问实例属性，类属性
#         print(self.age)
#         print(self.name)
#
#     @classmethod
#     def leifangfa(cls):
#         # 类方法可以访问类属性
#         print(cls.age)
#         # print(cls.name)
#
#     @staticmethod
#     def jingtaifangfa():
#         # 静态方法可以访问类属性
#         print(Person.age)
#         # print(Person.name)
#
#
# p = Person()
# # print(p.age)
# # print(Person.age)
#
# # p.shilifangfa()
# # p.leifangfa()
# p.jingtaifangfa()

# 4. 类的创建方式
# 4.1 常规方式
# 4.2 元类type创建

# def run(self):
#     print(f'self is {self}')
#
# d = type('dog', (), {'name': 'xiaohuang', 'run': run})



# 5. 类的创建时，元类的查找机制

# class Person:
#     """
#     这是一个Person类
#     """
#     pass
#
# p = Person()
# print(p.__dict__)
# print(Person.__doc__)


# 6. 类的描述
# class Person:
#     """
#     类描述可以写在这里，这是一个Person类
#     Attibutes:
#         count: 这是人的个数
#     """
#     count = 1
#
#
# print(help(Person))


# 7. 类属性的补充，私有化属性
class Person:
    pass
