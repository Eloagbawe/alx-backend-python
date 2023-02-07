#!/usr/bin/env python3
"""This file contains the measure_runtime function"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This function measures the total runtime
    of the async_comprehension four times in parallel
    and return it"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.perf_counter() - start
    return end
