import asyncio
import websockets


async def main():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"
        await websocket.send(message)
        print(f"Отправлено: {message}")

        for _ in range(5):
            response = await websocket.recv()
            print(response)


if __name__ == "__main__":
    asyncio.run(main())