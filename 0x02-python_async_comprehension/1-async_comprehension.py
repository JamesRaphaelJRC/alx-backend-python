#!/usr/bin/env python3
''' Defines a coroutine 'async_comprehension' '''
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    ''' Collects 10 numbers using an async comprehensing over 
        async_generator and return the 10 numbers
    '''
    random_nums = [i async for i in async_generator()]
    return random_nums
