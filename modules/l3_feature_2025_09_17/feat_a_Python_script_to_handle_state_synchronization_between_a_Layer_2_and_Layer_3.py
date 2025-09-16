import asyncio
import websockets

async def synchronize_state(l2_url, l3_url):
    async with websockets.connect(l2_url) as l2_socket, websockets.connect(l3_url) as l3_socket:
        while True:
            try:
                l2_state = await asyncio.wait_for(l2_socket.recv(), timeout=1)
                await l3_socket.send(l2_state)
                l3_ack = await asyncio.wait_for(l3_socket.recv(), timeout=1)
                if l3_ack != "ACK":
                    raise Exception("Layer 3 ACK failed")
            except asyncio.TimeoutError:
                print("Synchronization timeout")
            except websockets.ConnectionClosed:
                print("Connection closed")
                break
            except Exception as e:
                print(f"Synchronization error: {e}")
                break

if __name__ == "__main__":
    l2_url = "ws://localhost:8080/l2"
    l3_url = "ws://localhost:8081/l3"
    asyncio.run(synchronize_state(l2_url, l3_url))

