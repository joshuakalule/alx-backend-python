#!/usr/bin/env python3
"""Async generator comprehension."""


from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asyc_comprehension implementation."""
    return [i async for i in async_generator()]
