'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/4/1 10:23 
'''

class Animal:
    pass

class Person(Animal):
    pass

class Student(Person):
    pass


class A:
    def __init__(self):
        print('this is A')

    def say(self):
        print('say AAA')


class B:
    def __init__(self):
        print('this is B')

    def say(self):
        print('say BBB')


class C(A, B):
    pass



if __name__ == '__main__':
    c = C()
    print(c.say())
    # s = Student()
    # print(dir(s))
    # print(Student.mro())