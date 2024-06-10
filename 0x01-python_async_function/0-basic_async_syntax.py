#!/usr/bin/env python3
"""
PYTHON ASYNC
"""
from random import uniform
import asyncio


async def wait_random(max_delay=10.0):
    """
    Async function
    """
    n = uniform(0.0, max_delay)
    await asyncio.sleep(n)
    return n
