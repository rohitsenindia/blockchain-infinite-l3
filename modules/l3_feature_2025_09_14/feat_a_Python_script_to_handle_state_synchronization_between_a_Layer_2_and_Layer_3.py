import asyncio
import websockets

async def synchronize_state(l2_url, l3_url):
    async with websockets.connect(l2_url) as l2_ws, websockets.connect(l3_url) as l3_ws:
        l2_state = await l2_ws.recv()
        l3_state = await l3_ws.recv()
        if l2_state != l3_state:
            if len(l2_state) > len(l3_state):
                await l3_ws.send(l2_state)
            else:
                await l2_ws.send(l3_state)
            await asyncio.sleep(1)  #introduce a small delay for testing
            l2_state_updated = await l2_ws.recv()
            l3_state_updated = await l3_ws.recv()
            assert l2_state_updated == l3_state_updated

asyncio.run(synchronize_state("ws://localhost:8765", "ws://localhost:8766"))

