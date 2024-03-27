#!/usr/bin/env python3
"""
writng && measure_runtime coroutine to execute async_comprehension
4Xs in parallel
"""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Defeniining measure_runtime coroutine
    """
    start = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    end = time.time()

    lag = end - start
    return lag
