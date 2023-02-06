#!/usr/bin/env python3
"""This file contains the task_wait_n function"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This function spawns the task_wait_random n times with the
    specified max_delay
    """
    res = await asyncio.gather(*(task_wait_random(max_delay)
                                 for i in range(n)))
    return sorted(res)
