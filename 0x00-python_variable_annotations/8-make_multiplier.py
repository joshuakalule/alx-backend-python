#!/usr/bin/env python3
"""Annotations."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Annotate callbacks"""
    def func(num: float) -> float:
        return num * multiplier
    return func
