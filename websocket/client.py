import websockets
import asyncio

async def call_echo(ip: str, port: int, msg: str) -> list:
    uri = f"ws://{ip}:{port}/ws"
    async with websockets.connect(uri) as ws:
        await ws.send(msg)
        bytes_data = await ws.recv()
        str_data = str(bytes_data)
        await ws.close()
    
    print(str_data)

if __name__ == '__main__':
    msg = '{"method": "ping", "type": "data", "data": ["test1", "test2"]}'
    asyncio.run(call_echo('127.0.0.1', 8000, msg))