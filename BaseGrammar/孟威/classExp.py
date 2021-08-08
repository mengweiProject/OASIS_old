'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/4/2 13:21 
'''


class A:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
        self._single_underline = u'单个下划线'
        self.__double_underline = u'双下划线'

    def methodA(self):
        print("A 的method")
        print(self.__double_underline)


    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


class B(A):
    def methodB(self):
        print("B 的method")


class C(B):
    def methodC(self):
        print("C 的method")

if __name__ == '__main__':
    # c = C("weige", 18)
    # print(c.name)
    # c.methodC()
    # c.setName("伟哥")
    # print(c.getName())
    a = A()
    print(a.methodA())