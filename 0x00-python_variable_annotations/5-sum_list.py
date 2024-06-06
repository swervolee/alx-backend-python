#!/usr/bin/env python3
"""
Annotated python
"""
from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Adds up a list of floats
    """
    return reduce(lambda a, b: a + b, input_list)
