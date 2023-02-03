from decorators import do_twice, do_twice_with_return

"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Who Are You, Really? 
A great convenience when working with Python, especially in the interactive shell, 
is its powerful introspection ability. Introspection is the ability of an object to know about its own attributes at 
runtime. For instance, a function knows its own name and documentation 

The introspection works for functions you define yourself as well
"""


def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


@do_twice_with_return
def say_whee():
    print('Whee')


if __name__ == "__main__":
    print(print)
    print(print.__name__)
    print("help: ")
    print(help(print))

    print('******** about greeting ************')
    print(return_greeting)
    print(return_greeting.__name__)
    print("help:")
    print(help(return_greeting))

    """However, after being decorated, say_whee() has gotten very confused about its identity. It now reports being 
    the wrapper_do_twice() inner function inside the do_twice() decorator. Although technically true, this is not 
    very useful information. """

    print('******** about say whee ************')
    print(say_whee)
    print(say_whee.__name__)
    print("help:")
    print(help(say_whee))
