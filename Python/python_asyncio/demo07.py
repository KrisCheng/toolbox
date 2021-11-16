# demo-07, official event loop demo

import asyncio  
import time

async def compute(x, y):  
    print("Compute {} + {}...".format(x, y)) # 4.coroutine is running
    await asyncio.sleep(1.0) # 5.coroutine is suspended here
    return x + y # 6. coroutine is running

async def print_sum(x, y):  
    result = await compute(x, y)
    print("{} + {} = {}".format(x, y, result)) # 7. coroutine is done
    
start = time.time()  

# 1. get EventLoop
loop = asyncio.get_event_loop() 

# 2.create task object, which is the execute unit in the async context, registered into the event loop.
tasks = [
    asyncio.ensure_future(print_sum(0, 0)), 
    asyncio.ensure_future(print_sum(1, 1)),
    asyncio.ensure_future(print_sum(2, 2)),
]

# 3. loop is running, tasks registered to the loop
loop.run_until_complete(asyncio.wait(tasks))  

# 8. task is finished, loop stoped
loop.close()  

print("Total elapsed time {} s".format(time.time() - start))
