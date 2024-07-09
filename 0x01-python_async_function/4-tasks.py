#!/usr/bin/env python3
"""Task waiting."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn n coroutines of wait_random."""
    coro_list = list()
    for _ in range(n):
        coro_list.append(task_wait_random(max_delay))

    return sorted(await asyncio.gather(*coro_list))
