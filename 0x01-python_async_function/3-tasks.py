#!/usr/bin/env python3
"""
PYTHON ASYNC
"""
import asyncio
from typing import Callable


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Callable[[int], float]:
    """
    Return an async function
    """
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
