import asyncio
import aiohttp

async def synchronize_state(l2_url, l3_url, l2_api_key, l3_api_key):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{l2_url}/state", headers={"X-API-Key": l2_api_key}) as l2_resp:
            l2_state = await l2_resp.json()
        async with session.get(f"{l3_url}/state", headers={"X-API-Key": l3_api_key}) as l3_resp:
            l3_state = await l3_resp.json()
        
        if l2_state != l3_state:
            if l2_state['version'] > l3_state['version']:
                async with session.post(f"{l3_url}/update", json=l2_state, headers={"X-API-Key": l3_api_key}):
                    pass
            else:
                async with session.post(f"{l2_url}/update", json=l3_state, headers={"X-API-Key": l2_api_key}):
                    pass

        return l2_state

async def main():
    l2_url = "http://localhost:8080"
    l3_url = "http://localhost:9090"
    l2_api_key = "l2_api_key"
    l3_api_key = "l3_api_key"
    state = await synchronize_state(l2_url, l3_url, l2_api_key, l3_api_key)
    print(f"Synchronized state: {state}")

if __name__ == "__main__":
    asyncio.run(main())
