"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Simple Decorators
Now that you’ve seen that functions are just like any other object in Python, you’re ready to move
on and see the magical beast that is the Python decorator.

In effect, the name say_whee now points to the wrapper() inner function. Remember that you return wrapper as a
function when you call my_decorator(say_whee) However, wrapper() has a reference to the original say_whee() as func,
and calls that function between the two calls to print().

Put simply: decorators wrap a function, modifying its behavior.

Before moving on, let’s have a look at a second example. Because wrapper() is a regular Python function,
the way a decorator modifies a function can change dynamically. So as not to disturb your neighbors, the following
example will only run the decorated code during the day
If you try to call say_whee() after bedtime, nothing will happen.
"""
from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep

    return wrapper


def say_whee():
    print("Whee!")


say_whee = not_during_the_night(say_whee)

if __name__ == "__main__":
    say_whee()
    print(say_whee)
