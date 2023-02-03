from decorators import do_twice, do_twice_with_return

"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Returning Values From Decorated Functions 
What happens to the return value of decorated functions? Well, that’s up to
the decorator to decide. Let’s say you decorate a simple function as follows

To fix this, you need to make sure the wrapper function returns the return value of the decorated function.
"""


@do_twice_with_return
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


if __name__ == "__main__":
    print(return_greeting("Adam"))
    """The return value from the last execution of the function is returned. """
