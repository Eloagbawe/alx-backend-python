#!/usr/bin/env python3
"""This file contains the task_wait_random function"""

import asyncio
from typing import Any, Type

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """this function takes an integer max_delay and returns
    a asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
