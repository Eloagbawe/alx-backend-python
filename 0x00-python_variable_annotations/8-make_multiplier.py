#!/usr/bin/env python3
"""This file contains the make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function returns a float multiplier"""
    def multiply(x: float) -> float:
        """This function multiples a float by multiplier"""
        return multiplier * x
    return multiply
