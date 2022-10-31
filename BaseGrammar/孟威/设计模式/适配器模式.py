'''
@Project ：OASIS
@Author  ：孟威
@Date    ：2022/10/31 14:31

适配器模式


'''




class OldTravel:
    def ride_horse(self):
        print('骑马溜大街')


class NewTravel:
    def high_speed_rail(self):
        print('高铁出行，方便快捷')


class Adapter(NewTravel):
    def ride_horse(self):
        return self.high_speed_rail()


if __name__ == '__main__':
    new_t = Adapter()
    new_t.ride_horse()
    new_t.high_speed_rail()