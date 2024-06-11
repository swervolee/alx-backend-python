#!/usr/bin/env python3
"""
PYTHON ASYNC
"""
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """
    Generator
    """
    for i in range(10):
        yield random.uniform(0, 10)
