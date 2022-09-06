



class Country:
    area = None
    province = None
    __nuclear_weapon = False

    def __init__(self, name, population):
        self.name = name
        self.population = population


    def __print_have_nuclear_weapon(self):
        print(f'have nuclear weapon is {Country.__nuclear_weapon}')


class Common:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property       # 用来访问私有属性
    def age(self):
        return self.__age

    @age.setter     # 用来设置私有属性
    def age(self, age):
        self.__age = age



if __name__ == '__main__':
    c = Country('China', 16 * (10 ** 9))
    print(dir(c))
    c._Country__nuclear_weapon = True
    print(c._Country__nuclear_weapon)
    c._Country__print_have_nuclear_weapon()