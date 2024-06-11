#!/usr/bin/env python3
"""
PYTHON ASYNC
"""
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of
    executing async_comprehension four times concurrently.
    """
    s = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    elapsed = time.perf_counter() - s
    return elapsed
