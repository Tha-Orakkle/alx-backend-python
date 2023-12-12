#!/usr/bin/env python3
"""asynchronous coroutine that waits for a random delay"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay and the returns the delay time"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
