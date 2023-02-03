#!/usr/bin/env python3
"""This file contains the element_length function"""
from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function returns an iterable"""
    return [(i, len(i)) for i in lst]
