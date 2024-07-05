#!/usr/bin/env python3
"""Annotations Module"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Annotate sum of mixed types."""
    return float(sum(mxd_lst))
