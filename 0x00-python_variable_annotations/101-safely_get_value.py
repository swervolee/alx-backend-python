#!/usr/bin/env python3
"""
Python annotation
"""
from typing import Union, Mapping, Any, TypeVar


def safely_get_value(dct: Mapping, key: any,
                     default: Union[TypeVar, any] = None
                     ) -> Union[Any, TypeVar]:
    """
    Function augmentation
    """
    if key in dct:
        return dct[key]
    else:
        return default
