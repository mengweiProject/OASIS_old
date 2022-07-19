'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/14 9:37 
'''



class Feb:
    def __init__(self, n):
        self.num = n

        self.a = 0
        self.b = 1
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.current_index += 1
            return self.b
        else:
            raise StopIteration



if __name__ == '__main__':
    fb = Feb(5)
    for item in fb:
        print(item)
