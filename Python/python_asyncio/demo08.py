import requests
import asyncio
import time

async def counter():
    now = time.time()
    print("Started counter") # 1
    for i in range(0, 10):
        last = now
        await asyncio.sleep(0.001)
        now = time.time()
        print(f"{i}: Was asleep for {now - last}s") # 4

# run a counter during request
# call sync code in async context, no error but blocked.
async def main():
    t = asyncio.get_event_loop().create_task(counter())

    await asyncio.sleep(0)

    print("Sending HTTP request") # 2

    r = requests.get('http://example.com') # synchronous IO call, when calling this, counter paused

    print(f"Got HTTP response with status {r.status_code}") # 3

    await t

asyncio.get_event_loop().run_until_complete(main())