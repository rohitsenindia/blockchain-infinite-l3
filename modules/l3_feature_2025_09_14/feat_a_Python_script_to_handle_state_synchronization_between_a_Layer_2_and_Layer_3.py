import asyncio
import websockets

async def synchronize_state(l2_websocket_url, l3_websocket_url):
    async with websockets.connect(l2_websocket_url) as l2_ws, websockets.connect(l3_websocket_url) as l3_ws:
        while True:
            try:
                l2_state = await asyncio.wait_for(l2_ws.recv(), timeout=1)
                await l3_ws.send(l2_state)
                l3_ack = await asyncio.wait_for(l3_ws.recv(), timeout=1)
                if l3_ack != "ACK":
                    print(f"L3 ACK failed: {l3_ack}")
            except asyncio.TimeoutError:
                print("Synchronization timeout")
            except websockets.exceptions.ConnectionClosed:
                print("Connection closed")
                break
            except Exception as e:
                print(f"Error during synchronization: {e}")
                break

asyncio.run(synchronize_state("ws://l2_node:8080", "ws://l3_node:8081"))

