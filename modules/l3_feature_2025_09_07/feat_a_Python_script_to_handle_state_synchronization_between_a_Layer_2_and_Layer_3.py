import asyncio
import websockets

async def synchronize_state(l2_url, l3_url):
    async with websockets.connect(l2_url) as l2_websocket, websockets.connect(l3_url) as l3_websocket:
        while True:
            try:
                l2_state = await l2_websocket.recv()
                await l3_websocket.send(l2_state)
                l3_ack = await l3_websocket.recv()
                await l2_websocket.send(l3_ack)
            except websockets.ConnectionClosed:
                break
            except Exception as e:
                print(f"Synchronization error: {e}")
                break

async def main():
    l2_url = "ws://localhost:8080/l2"
    l3_url = "ws://localhost:8081/l3"
    await synchronize_state(l2_url, l3_url)

if __name__ == "__main__":
    asyncio.run(main())
