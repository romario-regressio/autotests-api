import asyncio
import websockets
from websockets.server import WebSocketServerProtocol


async def handler(websocket: WebSocketServerProtocol):
    message = await websocket.recv()
    print(f"Получено сообщение от пользователя: {message}")

    for i in range(1, 6):
        response = f"{i} Сообщение пользователя: {message}"
        await websocket.send(response)


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket сервер запущен на ws://localhost:8765")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())