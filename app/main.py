from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    cached_data = {}

    def wrapper(*args) -> Any:
        if args not in cached_data.keys():
            cached_data[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cached_data[args]
    return wrapper
