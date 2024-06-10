#!/usr/bin/env python3
"""
PYTHON ASYNC
"""
from random import uniform
import asyncio


async def wait_random(max_delay: int =10) -> float:
    """
    Async function
    """
    n: int = uniform(0.0, max_delay)
    await asyncio.sleep(n)
    return n
