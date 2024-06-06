#!/usr/bin/env python3
"""
Python annotations
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Annotation in python
    """
    return (k, v ** 2)
