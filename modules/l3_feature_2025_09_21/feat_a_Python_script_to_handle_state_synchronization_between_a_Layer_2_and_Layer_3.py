import asyncio
import websockets

async def synchronize_state(l2_url, l3_url):
    async with websockets.connect(l2_url) as l2_websocket, websockets.connect(l3_url) as l3_websocket:
        while True:
            l2_state = await l2_websocket.recv()
            try:
                l3_state = await asyncio.wait_for(l3_websocket.recv(), timeout=1)
                if l2_state != l3_state:
                    await l3_websocket.send(l2_state)
            except asyncio.TimeoutError:
                await l3_websocket.send(l2_state)
            except websockets.exceptions.ConnectionClosedOK:
                break

async def main():
    await synchronize_state("ws://localhost:8080/l2", "ws://localhost:8081/l3")

if __name__ == "__main__":
    asyncio.run(main())
