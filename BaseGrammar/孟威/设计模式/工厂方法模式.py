'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/31 14:17

工厂方法模式
同样隐藏了对象创建的细节，也不需要修改工厂类代码
但是，每增加一个具体的产品类，就必须增加一个具体的工厂类
'''


from abc import ABCMeta, abstractmethod

class Animal(object, metaclass=ABCMeta):
    @abstractmethod
    def jiaosheng(self):
        pass


class Dog(Animal):
    def jiaosheng(self):
        print('汪汪汪...')


class Cat(Animal):
    def jiaosheng(self):
        print('喵喵...')


class AnimalFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_animal(self):
        pass


class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()


if __name__ == '__main__':
    dogs = DogFactory()
    xiaojimao = dogs.create_animal()
    xiaojimao.jiaosheng()
