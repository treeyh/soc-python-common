# -*- encoding: utf-8 -*-

'''
@file           :ws_client.py
@description    :
@time           :2025-02-25 18:01:44
@author         :Tree
@version        :1.0
'''

import asyncio
import websockets

async def connect_and_receive():
    uri = "ws://47.100.103.85:8765"  # 连接到WebSocket服务器
    async with websockets.connect(uri) as websocket:
        print(f"已连接到 {uri}")
        while True:
            message = await websocket.recv()  # 接收服务器消息
            print(f"收到消息: {message}")

async def main():
    await connect_and_receive()

if __name__ == "__main__":
    asyncio.run(main())