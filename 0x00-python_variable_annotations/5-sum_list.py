#!/usr/bin/env python3
"""type-annotated function sum_list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list of floats and returns
    sum as a float"""
    return sum(input_list)
