import asyncio
import websockets

async def sync_state(l2_url, l3_url):
    async with websockets.connect(l2_url) as l2_ws, websockets.connect(l3_url) as l3_ws:
        while True:
            l2_state = await l2_ws.recv()
            try:
                await l3_ws.send(l2_state)
                ack = await l3_ws.recv()
                if ack != "ACK":
                    raise Exception("Synchronization failed")
            except websockets.exceptions.ConnectionClosed:
                print("Layer 3 connection lost. Retrying...")
                break
            except Exception as e:
                print(f"Synchronization error: {e}")
                break

async def main():
    await sync_state("ws://localhost:8080/l2", "ws://localhost:9090/l3")

if __name__ == "__main__":
    asyncio.run(main())
