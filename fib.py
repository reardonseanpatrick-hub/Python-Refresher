# fib.py

from functools import lru_cache
import time
from typing import Callable


def timer(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Finished in {elapsed:.7f}s: f({args[0]}) -> {result}")
        return result
    return wrapper


@lru_cache
@timer
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    fib(100)
