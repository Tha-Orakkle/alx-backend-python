#!/usr/bin/env python3
"""asynchronous coroutine that waits for a random delay"""
import asyncio
import random


async def wait_random(max_delay=10.0):
    """waits for a random delay and the returns the delay time"""
    delay = random.uniform(0, 10.0)
    await asyncio.sleep(delay)
    return delay
