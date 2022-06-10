


def generator(n):
    for i in range(n):
        yield i


if __name__ == '__main__':
    tasks = generator(10)
    for task in tasks:
        print(task)