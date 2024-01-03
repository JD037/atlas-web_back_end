#!/usr/bin/env python3

"""
a coroutine async_generator that yields a random number
between 0 and 10 every second for 10 times.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Generate random numbers asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
