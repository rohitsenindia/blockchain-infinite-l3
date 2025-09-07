import asyncio
import websockets

async def synchronize_state(l2_uri, l3_uri):
    async with websockets.connect(l2_uri) as l2_ws, websockets.connect(l3_uri) as l3_ws:
        while True:
            try:
                l2_state = await l2_ws.recv()
                await l3_ws.send(l2_state)
                l3_ack = await l3_ws.recv()
                await l2_ws.send(l3_ack)

            except websockets.exceptions.ConnectionClosed:
                print("Connection closed. Reconnecting...")
                await asyncio.sleep(5)
            except Exception as e:
                print(f"An error occurred: {e}")
                await asyncio.sleep(5)

async def main():
    await synchronize_state("ws://l2_node:8080", "ws://l3_node:8081")

if __name__ == "__main__":
    asyncio.run(main())
