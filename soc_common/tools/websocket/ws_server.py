# -*- encoding: utf-8 -*-

'''
@file           :ws_server.py
@description    :
@time           :2025-02-25 17:45:54
@author         :Tree
@version        :1.0
'''

import asyncio
import websockets
import datetime

async def handle_client(websocket, path: str = None):
    client_ip = websocket.remote_address[0]  # 获取客户端IP地址
    print(f"客户端 {client_ip} 已连接")
    print(websocket.remote_address)

    try:
        while True:
            await asyncio.sleep(1)  # 每隔1秒执行一次
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"[{now}] 客户端IP: {client_ip}"
            await websocket.send(message)  # 向客户端发送消息
            print(message)  # 在服务端输出消息

    except websockets.exceptions.ConnectionClosedOK:
        print(f"客户端 {client_ip} 已断开连接")
    except Exception as e:
        print(f"发生错误: {e}")

async def main():
    async with websockets.serve(handle_client, "0.0.0.0", 8765):
        print("WebSocket 服务已启动，监听端口 8765...")
        await asyncio.Future()  # 保持服务运行

if __name__ == "__main__":
    asyncio.run(main())