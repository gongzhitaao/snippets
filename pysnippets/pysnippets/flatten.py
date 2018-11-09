from collections.abc import Iterable


def flatten(items):
    """
    Flatten list of arbitrary depth.
    """
    if isinstance(items, Iterable) and not isinstance(items, (str, bytes)):
        for x in items:
            for sub_x in flatten(x):
                yield sub_x
    else:
        yield items
