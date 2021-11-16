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
        print(f"{i}: Was asleep for {now - last}s") # 3

async def main():
    t = asyncio.get_event_loop().create_task(counter())

    await asyncio.sleep(0)

    def send_request():
        print("Sending HTTP request") # 2
        r = requests.get('http://example.com')
        print(f"Got HTTP response with status {r.status_code}") # 4

    '''
    run_in_executor, counter was not blocked by the HTTP request.
    run in the default loop's executor with first parm as None
    a good way to use sync code in the context of async
    '''
    await asyncio.get_event_loop().run_in_executor(None, send_request)

    await t

asyncio.get_event_loop().run_until_complete(main())