'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/31 13:46

简单工厂模式
隐藏了对象创建的细节，由传入的对象决定创建哪种实例

'''

import abc


class Animal(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def jiaosheng(self):
        pass


class Dog(Animal):
    def jiaosheng(self):
        print('汪汪汪...')


class Cat(Animal):
    def jiaosheng(self):
        print('我们一起学猫叫，一起喵喵喵...')


class Chicken(Animal):
    def jiaosheng(self):
        print('hello 大家好，我是练习时长两年半的...')


class AnimalFactory:
    def create_animal(self, animal_str):
        if animal_str == 'DOG':
            return Dog()
        elif animal_str == 'DOG':
            return Cat()
        else:
            return Chicken()


if __name__ == '__main__':
    animal_f = AnimalFactory()
    animal = animal_f.create_animal('CHICKEN')
    animal.jiaosheng()