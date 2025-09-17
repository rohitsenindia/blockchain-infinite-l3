import asyncio
import websockets

async def synchronize_state(l2_url, l3_url):
    async with websockets.connect(l2_url) as l2_socket, websockets.connect(l3_url) as l3_socket:
        while True:
            l2_state = await l2_socket.recv()
            try:
                l3_state = await asyncio.wait_for(l3_socket.recv(), timeout=1)
                if l2_state != l3_state:
                    await l3_socket.send(l2_state)
            except asyncio.TimeoutError:
                await l3_socket.send(l2_state)
            except websockets.exceptions.ConnectionClosedOK:
                break

asyncio.run(synchronize_state("ws://l2_node:8080", "ws://l3_node:8081"))
