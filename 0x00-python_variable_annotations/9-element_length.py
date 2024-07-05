#!/usr/bin/env python3
"""Annotations module."""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate task 9"""
    return [(i, len(i)) for i in lst]
