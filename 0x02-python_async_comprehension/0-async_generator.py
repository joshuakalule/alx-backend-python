#!/usr/bin/env python3
"""Asnyc generator."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Implement async generator."""
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
