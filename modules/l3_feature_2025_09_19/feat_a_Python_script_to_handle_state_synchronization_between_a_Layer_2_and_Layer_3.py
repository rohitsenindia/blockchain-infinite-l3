import asyncio
import aiohttp

async def synchronize_state(l2_api_url, l3_api_url, state_key):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{l2_api_url}/state/{state_key}") as l2_resp:
            l2_state = await l2_resp.json()
        async with session.get(f"{l3_api_url}/state/{state_key}") as l3_resp:
            l3_state = await l3_resp.json()
        if l2_state != l3_state:
            async with session.put(f"{l3_api_url}/state/{state_key}", json=l2_state) as update_resp:
                if update_resp.status != 200:
                    print(f"Error updating L3 state: {await update_resp.text()}")

async def main():
    l2_url = "http://localhost:8080"
    l3_url = "http://localhost:9090"
    await synchronize_state(l2_url, l3_url, "global_counter")

if __name__ == "__main__":
    asyncio.run(main())
