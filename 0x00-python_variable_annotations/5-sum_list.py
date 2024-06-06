#!/usr/bin/env python3
"""
Annotated python
"""
from functools import reduce


def sum_list(input_list: list[float]) -> float:
    """
    Adds up a list of floats
    """
    return reduce(lambda a, b: a + b, input_list)
