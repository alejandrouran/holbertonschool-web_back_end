#!/usr/bin/env python3
""" should measure the total runtime and return it. """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time for four parallel comprehensions """
    tasks = []
    start_time = time.time()
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
        await asyncio.gather(*tasks)
        end_time = time.time()
        return end_time - start_time
