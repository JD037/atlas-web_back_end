#!/usr/bin/env python3

"""
a function make_multiplier that takes a float and returns
a function multiplying a float by the given multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by a given multiplier. """
    return lambda x: x * multiplier
