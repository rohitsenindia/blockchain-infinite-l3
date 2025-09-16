import asyncio
import websockets

async def synchronize_state(l2_url, l3_url):
    async with websockets.connect(l2_url) as l2_websocket, websockets.connect(l3_url) as l3_websocket:
        while True:
            l2_state = await l2_websocket.recv()
            try:
                await l3_websocket.send(l2_state)
                ack = await l3_websocket.recv()
                if ack != "ACK":
                    raise Exception("Synchronization failed")
            except websockets.exceptions.ConnectionClosed:
                print("Layer 3 connection lost. Retrying...")
                await asyncio.sleep(5)
            except Exception as e:
                print(f"Synchronization error: {e}")
                break

async def main():
    await synchronize_state("ws://l2_node:8080", "ws://l3_node:8081")

if __name__ == "__main__":
    asyncio.run(main())

