#!/usr/bin/env python3
"""
Annotated python
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a callable
    """
    def inner(x: float) -> float:
        """
        Multiplies a float by multiplier
        """
        return x * multiplier

    return inner
