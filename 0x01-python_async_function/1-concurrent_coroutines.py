#!/usr/bin/env python3
"""This file contains the wait_n function"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This function spawns the wait_random n times with the
    specified max_delay
    """
    res = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    # return sorted(res)
    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            if res[i] > res[j]:
                res[i], res[j] = res[j], res[i]
    return res
