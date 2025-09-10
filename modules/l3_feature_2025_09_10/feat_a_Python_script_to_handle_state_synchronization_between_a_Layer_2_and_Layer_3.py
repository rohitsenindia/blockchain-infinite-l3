import asyncio
import websockets

async def synchronize_state(l2_url, l3_url):
    async with websockets.connect(l2_url) as l2_ws, websockets.connect(l3_url) as l3_ws:
        while True:
            l2_state = await l2_ws.recv()
            try:
                l3_state = await l3_ws.recv()
                if l2_state != l3_state:
                    await l3_ws.send(l2_state)
            except websockets.exceptions.ConnectionClosed:
                print("Layer 3 connection lost. Reconnecting...")
                l3_ws = await websockets.connect(l3_url)
            except Exception as e:
                print(f"Error during synchronization: {e}")

async def main():
    l2_websocket_url = "ws://localhost:8080/l2"
    l3_websocket_url = "ws://localhost:8081/l3"
    await synchronize_state(l2_websocket_url, l3_websocket_url)


if __name__ == "__main__":
    asyncio.run(main())
