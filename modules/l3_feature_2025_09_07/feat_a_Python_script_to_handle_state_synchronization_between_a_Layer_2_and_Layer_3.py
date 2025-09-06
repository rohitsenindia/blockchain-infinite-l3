import asyncio
import websockets

async def synchronize_state(l2_url, l3_url):
    async with websockets.connect(l2_url) as l2_websocket, websockets.connect(l3_url) as l3_websocket:
        l2_state = await l2_websocket.recv()
        l3_state = await l3_websocket.recv()
        if l2_state != l3_state:
            if len(l2_state) > len(l3_state):
                await l3_websocket.send(l2_state)
            else:
                await l2_websocket.send(l3_state)
            await asyncio.sleep(1) # Adjust as needed
            await synchronize_state(l2_url, l3_url)

asyncio.run(synchronize_state("ws://l2_node:8080", "ws://l3_node:8081"))

