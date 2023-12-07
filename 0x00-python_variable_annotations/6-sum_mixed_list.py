#!/usr/bin/env python3
"""type-annotated  fucntion sum_mixed_list"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """takes a list of floats and ints and returns sum"""
    return sum(mxd_list)
