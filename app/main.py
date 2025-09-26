from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    cached_args = []
    cached_results = []

    def wrapper(*args) -> Any:
        if args not in cached_args:
            cached_args.append(args)
            cached_results.append(func(*args))
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cached_results[cached_args.index(args)]
    return wrapper
