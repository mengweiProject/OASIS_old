'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/7/13 14:00 
'''


class Move:
    def __init__(self):
        self.road = "东西南北路"

    @classmethod
    def run(cls, speed):
        # @classmethod装饰器的作用就是让此方法可以不用把类实例化，即可通过类名进行调用
        print("以{}m/s的速度奔跑".format(speed))

    def walk(self, speed):
        print("以{}m/s的速度散步".format(speed))

    @property
    def address(self):
        return self.road


if __name__ == '__main__':
    # Move.run(9)
    # Move.walk(1)
    # w = Move()
    # w.walk(1)
    # t = {1, 2, 1, 3}
    # print(t)
    # t2 = set([1, 2, 3, 4, 1, 2, 3])
    # print(t2)
    # f = 12234323.456344378
    # print("{0:.3f}".format(f))
    for i in range(1, 60000):
        print(chr(i))
    # print(ord('ퟻ'))