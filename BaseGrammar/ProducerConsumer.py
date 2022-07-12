'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/5 10:10
生产消费者
'''

from multiprocessing import Process, Manager, Event
from time import sleep

from time_helper import time_consume


def structure_tasks():
    return [i for i in range(10)]


def worker(n):
    print(f'任务{n}--start...')
    sleep(n)
    print(f'任务{n}--end...')
    return n ** 2


class P(Process):
    def __init__(self, queue, tasks, event):
        super().__init__()
        self.queue = queue
        self.tasks = tasks
        self.prepare_task_done = event

    def run(self) -> None:
        if len(self.tasks) == 0:
            self.tasks = structure_tasks()

        for task in self.tasks:
            print('将任务存储到队列')
            self.queue.put(task)

        print('任务队列构造完成，可以开始子任务...')
        self.prepare_task_done.set()
        print()


class C(Process):
    def __init__(self, queue, event):
        super().__init__()
        self.queue = queue
        self.event = event

    def run(self):
        self.event.wait()
        print('子任务开始...')
        result_dict = {}
        while True:
            if not self.queue.empty():
                task = self.queue.get()
                worker(task)
            else:
                break


if __name__ == '__main__':
    q = Manager().Queue()
    event = Event()
    p = P(q, [], event)
    c = C(q, event)
    p.start()
    c.start()
    p.join()
    c.join()
