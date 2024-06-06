#!/usr/bin/env python3
"""
Annotated python
"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Prints a list
    """
    return [(i, len(i)) for i in lst]
