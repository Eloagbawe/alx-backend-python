#!/usr/bin/env python3
"""This file contains the sum_list function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """This function returns the sum of a list as a float"""
    sum: float = 0
    for elem in input_list:
        sum += elem
    return sum
