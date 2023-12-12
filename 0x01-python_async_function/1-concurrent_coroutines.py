#!/usr/bin/env python3
"""
async function that import and spawns the wait_random
coroutine n times
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns a list of the delay seconds
    in ascending order
    """
    delays = []

    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_tasks = await asyncio.gather(*tasks)
    delays.extend(completed_tasks)
    return sorted(delays)
