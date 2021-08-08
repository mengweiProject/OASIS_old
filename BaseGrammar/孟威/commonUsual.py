'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/7/16 9:54 
'''



# list comprehension
def listComprehension():
    l = [i for i in range(10)]
    print(l)


# list generator
def listGenerator():
    l = (i for i in range(10))
    print(l)
    for i in l:
        print(i)


def generatorYield():
    n = 1
    while True:
        yield n
        n += 1
        if n > 10:
            return n


if __name__ == '__main__':
    # listGenerator()
    generator = generatorYield()
    for i in range(10):
        print(next(generator))