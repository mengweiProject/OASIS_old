'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/31 10:30

在一个项目/工程中，为了减少某些对象的创建/销毁的开销，只允许一个实例存在，这时候就用到了单例模式。
单例模式的几种实现方式
1. 以模块化的方式实现，在一个模块中创建好实例对象。当其他地方需要用到这个对象，直接引入。
这个实例也是这个类对象的全局访问点，可以避免重复创建
2. 装饰器函数/类装饰器实现
3. 重写__new__方法等
'''



class Dog:
    _instance = None
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == '__main__':
    jinmao = Dog('小鸡毛', 3)
    print(jinmao, jinmao.name, jinmao.age)

    ladeduo = Dog('拉的多', 3.5)
    print(ladeduo, ladeduo.name, ladeduo.age)