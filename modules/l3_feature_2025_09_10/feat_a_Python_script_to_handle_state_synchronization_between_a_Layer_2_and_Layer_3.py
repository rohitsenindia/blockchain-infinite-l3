import asyncio
import websockets

async def synchronize_state(l2_url, l3_url):
    async with websockets.connect(l2_url) as l2_websocket, websockets.connect(l3_url) as l3_websocket:
        while True:
            l2_state = await l2_websocket.recv()
            try:
                l3_state = await l3_websocket.recv()
                if l2_state != l3_state:
                    await l3_websocket.send(l2_state)
            except websockets.exceptions.ConnectionClosed:
                await l3_websocket.send(l2_state)
            await asyncio.sleep(1)

async def main():
    l2_url = "ws://localhost:8080/l2"
    l3_url = "ws://localhost:9090/l3"
    await synchronize_state(l2_url, l3_url)

if __name__ == "__main__":
    asyncio.run(main())

