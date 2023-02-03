"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Reusing Decorators
"""
from decorators import do_twice


@do_twice
def say_whee():
    print("Whee!")


# say_whee = my_decorator(say_whee)

if __name__ == "__main__":
    say_whee()
    print(say_whee)
