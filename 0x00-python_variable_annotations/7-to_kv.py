#!/usr/bin/env python3
"""This file contains the to_kv function"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function returns a tuple"""
    square: float = v * v
    return (k, square)
