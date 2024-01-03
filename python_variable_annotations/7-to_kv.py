#!/usr/bin/env python3

"""
a function to_kv that takes a string and an int/float, and returns
a tuple with the string and the square of the number
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple of a string and the square of a number. """
    return (k, float(v**2))
