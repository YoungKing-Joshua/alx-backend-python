#!/usr/bin/env python3
"""
    define wait_n function
"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        spawning random n times with specify max_delay
    """
    tasks = [wait_random(max_delay) for x in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
