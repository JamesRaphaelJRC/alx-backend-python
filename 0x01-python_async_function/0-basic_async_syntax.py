#!/usr/bin/env python3
''' Defines an asynchronous coroutine '''
import asyncio
import random

async def wait_random(max_delay: int = 10):
    ''' Waits for a random delay beween 0 and max_delay and returns it '''
    delay_time = random.triangular(0, max_delay)
    asyncio.sleep(delay_time)
    return delay_time
