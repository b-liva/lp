import functools
import time


def slow_down(func):
    """Sleep 1 second before calling the function"""
    """The @slow_down decorator always sleeps for one second. Later, you’ll see how to control the rate by passing an 
    argument to the decorator """

    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper_slow_down
