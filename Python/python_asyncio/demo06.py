# demo-06, decorator coroutine && native coroutine

import asyncio

# Python 3.4, deprecated in Python 3.8, and removed in 3.10. not recommended.
@asyncio.coroutine
def hello_decorator():
    print("Hello world!")
    r = yield from asyncio.sleep(1)
    print("Hello again!")


# Python 3.5+
 def hello_native():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")


# get EventLoop
loop = asyncio.get_event_loop()

# run coroutine
loop.run_until_complete(hello_native())

loop.run_until_complete(hello_decorator())

loop.close()

