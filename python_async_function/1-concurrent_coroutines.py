#!/usr/bin/env python3

"""
Import wait_random from the previous file and write an async routine
wait_n that takes in two int arguments: n and max_delay.
Spawn wait_random n times with the specified max_delay
and return the list of delays in ascending order
"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay."""
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
