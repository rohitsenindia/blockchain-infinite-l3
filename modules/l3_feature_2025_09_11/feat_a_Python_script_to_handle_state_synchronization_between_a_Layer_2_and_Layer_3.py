import asyncio
import websockets

async def synchronize_state(l2_url, l3_url):
    async with websockets.connect(l2_url) as l2_ws, websockets.connect(l3_url) as l3_ws:
        l2_state = await l2_ws.recv()
        l3_state = await l3_ws.recv()
        if l2_state != l3_state:
            if hash(l2_state) > hash(l3_state):
                await l3_ws.send(l2_state)
            else:
                await l2_ws.send(l3_state)
            await asyncio.sleep(1) #Simulate syncing delay
            await synchronize_state(l2_url, l3_url)


asyncio.run(synchronize_state("ws://l2_node:8080", "ws://l3_node:8081"))
