import random

from decorators import register, PLUGINS

"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Registering Plugins 
Decorators don’t have to wrap the function they’re decorating. They can also simply register that 
a function exists and return it unwrapped. This can be used, for instance, to create a light-weight plug-in 
architecture 

The @register decorator simply stores a reference to the decorated function in the global PLUGINS dict. Note that you 
do not have to write an inner function or use @functools.wraps in this example because you are returning the original 
function unmodified. 

The randomly_greet() function randomly chooses one of the registered functions to use. Note that the PLUGINS 
dictionary already contains references to each function object that is registered as a plugin Using the @register 
decorator, you can create your own curated list of interesting variables, effectively hand-picking some functions 
from globals() """


@register
def say_hello(name):
    return f"Hello {name}"


@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)


if __name__ == "__main__":
    print(PLUGINS)
    randomly_greet('Alice')
    print(globals())
