# tornado version 6.1
# Compatible with asyncio

from tornado.ioloop import IOLoop

async def foo():
    print(123)

IOLoop.current().run_sync(foo)  # 123