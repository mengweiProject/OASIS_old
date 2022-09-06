'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/25 16:38 
'''


class Dog:
    num_leg = 4

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    d1 = Dog('tom')
    d2 = Dog('john')
    print(Dog.num_leg, d1.num_leg, d2.num_leg)

    d1.num_leg = 6
    print(Dog.num_leg, d1.num_leg, d2.num_leg)

    Dog.num_leg = 7
    print(Dog.num_leg, d1.num_leg, d2.num_leg)


