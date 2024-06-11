#!/usr/bin/env python3
"""
PYTHON ASYNC
"""
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """
    Generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
