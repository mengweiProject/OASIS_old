'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/31 14:17 
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
