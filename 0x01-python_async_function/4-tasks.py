#!/usr/bin/env python3
"""
Defines a concurrent execution function
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' Spawns the 'wait_random' async function 'n' number of times with the
        the specified 'max_delay'.

        Return: A list of delays in ascending order
    '''
    spawn_list = [task_wait_random(max_delay) for i in range(n)]
    delay_list = await asyncio.gather(*spawn_list)
    return sorted(delay_list)
