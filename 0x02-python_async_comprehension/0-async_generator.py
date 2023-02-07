#!/usr/bin/env python3
"""This file contains the async_generator function"""

import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """This function will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 1
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
