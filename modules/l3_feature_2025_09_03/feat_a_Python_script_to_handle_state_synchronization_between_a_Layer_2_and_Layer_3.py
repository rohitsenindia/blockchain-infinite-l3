import asyncio
import websockets

async def synchronize_state(l2_url, l3_url):
    async with websockets.connect(l2_url) as l2_ws, websockets.connect(l3_url) as l3_ws:
        while True:
            l2_state = await l2_ws.recv()
            await l3_ws.send(l2_state)
            l3_state = await l3_ws.recv()
            await l2_ws.send(l3_state)

async def main():
    l2_url = "ws://localhost:8080/l2"
    l3_url = "ws://localhost:8081/l3"
    await synchronize_state(l2_url, l3_url)

if __name__ == "__main__":
    asyncio.run(main())
