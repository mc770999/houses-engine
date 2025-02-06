import functools
from time import sleep
from random import uniform


def add_delay(delay):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            delay_this = uniform(1, delay)
            print(f"Waiting {delay_this} seconds before calling {func.__name__}...")
            sleep(delay)  # Pause execution for `seconds`
            return func(*args, **kwargs)
        return wrapper
    return decorator
