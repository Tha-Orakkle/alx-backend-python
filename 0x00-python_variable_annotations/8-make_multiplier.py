#!/usr/bin/env python3
"""type-annotated function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier
    """
    def float_multiplier(f: float) -> float:
        """multiplies a float by a multiplier"""
        return float(f * multiplier)
    return float_multiplier
