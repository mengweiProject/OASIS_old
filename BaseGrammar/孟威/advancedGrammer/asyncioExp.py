# @Time : 2021/8/3 21:40
# @Author: 小脑斧
# @File : asyncioExp.py

from time import sleep, time
import asyncio

loop = asyncio.get_event_loop()


# async def my_sleep():
#     sleep(3)


async def consume_time():
    print('start consume_time')
    await asyncio.sleep(3)
    return 3


def run():
    # s_time = time()
    tasks = [consume_time() for _ in range(2)]
    # results = loop.run_until_complete(asyncio.wait(tasks))
    loop = asyncio.get_event_loop()
    loop.run_in_executor()
    # f_time = time()
    print(results)

    # print(f_time - s_time)
    return 'main end...'


if __name__ == '__main__':
    print(run())