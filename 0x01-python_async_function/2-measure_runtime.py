#!/usr/bin/env python3
''' Defines function that calculates the time taken to perform
    a task
'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Measures the total execution time for
                        wait_n(n, max_delay)
        Return:
                total time taken
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return end_time - start_time
