from decorators import do_twice

"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Who Are You, Really? 
A great convenience when working with Python, especially in the interactive shell, 
is its powerful introspection ability. Introspection is the ability of an object to know about its own attributes at 
runtime. For instance, a function knows its own name and documentation 

The introspection works for functions you define yourself as well

To fix this, decorators should use the @functools.wraps decorator, which will preserve information about the original 
function. Update decorators.py again """


@do_twice
def say_whee():
    print('Whee')


if __name__ == "__main__":
    # Much better! Now say_whee() is still itself after decoration.
    print('******** about say whee ************')
    print(say_whee)
    print(say_whee.__name__)
    print("help:")
    print(help(say_whee))
