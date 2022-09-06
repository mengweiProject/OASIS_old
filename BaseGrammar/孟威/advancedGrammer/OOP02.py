"""
super（）用法
"""


class A:
    def __init__(self, age):
        self.age = age

    def say(self, name):
        print(f'{name} say hello...')


class B(A):
    def __init__(self, age, height):
        super(B, self).__init__(age)
        self.height = height


    def say(self, name, target):
        super(B, self).say(name)
        print(f'{name} say hello to {target}')



if __name__ == '__main__':
    # a = A()
    # a.say('xiaohuang', 'xiaolv')
    b = B()
    b.say('xiaohuang', 'xiaolv')