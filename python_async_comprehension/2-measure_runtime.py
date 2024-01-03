#!/usr/bin/env python3

"""
Import async_comprehension from the previous file and write a
measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
"""

import asyncio
import time

async_comprehensions = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Measure the runtime of async_generator"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehensions() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
