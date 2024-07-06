#!/usr/bin/env python3
"""Annotate advanced"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Annotate sefe first element."""
    if lst:
        return lst[0]
    else:
        return None
