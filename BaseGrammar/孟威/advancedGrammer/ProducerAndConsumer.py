"""
生产消费者
"""

from multiprocessing import Process, Manager, active_children
import random
import time


class Producer(Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(6):
            r = random.randint(1, 10)
            time.sleep(1)
            self.queue.put(r)
            print(f'add data {r}')


class Consumer(Process):
    def __init__(self,queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            if not self.queue.empty():
                data = self.queue.get()
                print(f'consumer get data: {data}')


if __name__ == '__main__':
    q = Manager().Queue()
    p = Producer(q)
    c = Consumer(q)
    p.start()
    c.start()
    p.join()
    c.join()
    print('main process end...')
