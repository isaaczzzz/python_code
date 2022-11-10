from sanic import Sanic
from sanic import Request, Websocket
from sanic.log import logger
import sys
import json

ip = sys.argv[1]
port = int(sys.argv[2])

app = Sanic('WS')

def echo(data):
    return data

async def register(req, ws, data):
    # 数据库保存
    # 打印测试
    print(data)
    return True

@app.websocket('/ws')
async def deconstruct(req, ws):
    while True:
        receive_data = await ws.recv()
        logger.info(f'recv: {receive_data}')
        dict = json.loads(receive_data)
        
        method = dict['method']
        type = dict['type']

        if type == 'data':
            data = dict['data']
        elif type == 'command':
            command = dict['command']

        if method == 'ping':
            await ws.send("pong")
        elif method == 'register':
            if(register(req, ws, data)):
                await ws.send(1)
                
if __name__ == '__main__':
    app.run(host=ip, port=port)