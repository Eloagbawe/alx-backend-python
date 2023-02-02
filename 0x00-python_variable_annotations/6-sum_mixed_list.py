#!/usr/bin/env python3
"""This file contains the sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function takes a list of mixed types and
    returns the sum of values as a float
    """
    sum: float = 0
    for num in mxd_lst:
        sum += num

    return sum
