import asyncio
import websockets

async def synchronize_state(l2_uri, l3_uri):
    async with websockets.connect(l2_uri) as l2_websocket, websockets.connect(l3_uri) as l3_websocket:
        l2_state = await l2_websocket.recv()
        l3_state = await l3_websocket.recv()
        if l2_state != l3_state:
            if len(l2_state) > len(l3_state):
                await l3_websocket.send(l2_state)
            else:
                await l2_websocket.send(l3_state)
            await asyncio.sleep(1)
            await synchronize_state(l2_uri, l3_uri)


async def main():
    await synchronize_state("ws://localhost:8765", "ws://localhost:9876")


if __name__ == "__main__":
    asyncio.run(main())
