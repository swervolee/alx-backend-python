#!/usr/bin/env python3
"""
PYTHON ASYNC
"""
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[int, None, None]:
    """
    Generator
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
