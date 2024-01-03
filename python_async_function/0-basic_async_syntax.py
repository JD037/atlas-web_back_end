#!/usr/bin/env python3

"""
an asynchronous coroutine wait_random that takes an integer argument
max_delay (default value of 10), waits for a random delay
between 0 and max_delay seconds, and returns the delay
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return the delay."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
