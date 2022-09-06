'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/20 9:49 
'''


from sanic import Sanic

from sanic.response import json


app = Sanic()

@app.route('/')
async def test(request):
    msg = {'msg': 'hello sanic'}
    return json(msg, ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8999)
