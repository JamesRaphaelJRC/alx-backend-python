#!/usr/bin/env python3
''' Defines a multiple coroutine executing function '''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    ''' Spawns the wait_random async function 'n' number of times with the
        the specified max_delay.

        Return: The list of delays in ascending order
    '''
    spawn_list = [wait_random(max_delay) for i in range(n)]
    delay_list = await asyncio.gather(*spawn_list)
    return sorted(delay_list)
