#!/usr/bin/env python3

"""
Toroutine async_generator with 10 iterations. Asynchronously waits for 
1 second each time, then yields a random number 
between 0 and 10 using the random module.
"""



import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Looping 10Xs with a time interval
    of 1 seconds between each iteration.
    """
    for n in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
