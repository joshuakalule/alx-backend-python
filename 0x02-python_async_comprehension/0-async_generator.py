#!/usr/bin/env python3
"""Asnyc generator."""

import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """Implement async generator."""
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
