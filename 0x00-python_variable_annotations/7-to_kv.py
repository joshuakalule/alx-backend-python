#!/usr/bin/env python3
"""Annotations module."""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Annotate to_kv"""
    return (k, v**2)
