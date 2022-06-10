'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/6/10 15:31 
'''



import asyncio


async def run(n):
    await asyncio.sleep(1)
    print('run 函数：', n)
    return f'run 函数返回值为：{n}'


if __name__ == '__main__':
    r = run(1)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(r)
    # loop.g

    print('end...')