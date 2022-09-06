"""
queue：用于多线程之间数据通信
multiprocessing.Queue：用于子进程之间通信
multiprocessing.Manager().Queue()：用于多进程之间
"""


import os
from multiprocessing import Process, Manager, Event, Queue
import multiprocessing
# import queue
from time import sleep

from time_helper import time_consume


class Producer(Process):
    def __init__(self, queue, tasks, event):
        super().__init__()
        self.queue = queue
        self.tasks = tasks
        self.prepare_task_done = event

    def run(self) -> None:
        if len(self.tasks) == 0:
            self.tasks = structure_tasks()
        for task in self.tasks:
            print(f'producer begin to add task...{task}')
            sleep(1)
            self.queue.put(task)
        # 待任务列表完全构造完成，通知子任务可以开始工作...
        self.prepare_task_done.set()
        print('sub process can start working...')


class Consumer(Process):
    def __init__(self, queue, event):
        super().__init__()
        self.queue = queue
        self.event = event

    def run(self) -> None:
        # 等待任务列表完全准备完毕后，再开始执行子任务
        # self.prepare_task_done.Event().wait
        self.event.wait()
        print('sub process start to get work...')
        while True:
            if not self.queue.empty():
                task = self.queue.get()
                print(f'run obtain task: {task}')
                worker(task)
            else:
                sleep(1)
                # print(f'tasks list is empty...waitting for adding task')
                print('tasks list is empty, prepare to exit...')
                break



def worker(n):
    sleep(2)
    print(f'sub process pid is {os.getpid()}, data is {n}')
    return n


def structure_tasks():
    tasks = [i for i in range(3)]
    return tasks


@time_consume
def run_main():
    q = Manager().Queue()
    event = Event()
    producer = Producer(q, [], event)
    consumer = Consumer(q, event)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()



if __name__ == '__main__':
    run_main()