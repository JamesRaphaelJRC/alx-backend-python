#!/usr/bin/env python3
''' Defines a coroutine 'measure_time' '''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Executes async_comprehension 4 times in parallel
        an measures and return the total runtime
    '''
    start_time = time.time()
    executions = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*executions)
    end_time = time.time()

    return end_time - start_time
