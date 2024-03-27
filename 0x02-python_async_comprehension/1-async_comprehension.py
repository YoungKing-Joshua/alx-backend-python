#!/usr/bin/env python3
"""
   Coroutine async_comprehension takes no arguments
"""


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Function return 10 random figures
    """
    result = [num async for num in async_generator()]
    return result
