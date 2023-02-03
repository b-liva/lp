"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Decorating Functions With Arguments

Say that you have a function that accepts some arguments. Can you still decorate
it? The problem is that the inner function wrapper_do_twice() does not take any arguments, but name="World" was
passed to it. You could fix this by letting wrapper_do_twice() accept one argument, but then it would not work for
the say_whee() function you created earlier.

The solution is to use *args and **kwargs in the inner wrapper function. Then it will accept an arbitrary number of
positional and keyword arguments. Rewrite decorators.py as follows: The wrapper_do_twice() inner function now accepts
any number of arguments and passes them on to the function it decorates. Now both your say_whee() and greet()
examples works """
from decorators import do_twice


@do_twice
def say_whee():
    print('Whee!')


@do_twice
def greet(name):
    print(f"Hello {name}")


# say_whee = my_decorator(say_whee)

if __name__ == "__main__":
    say_whee()
    print(say_whee)
    greet("world")
    print(greet)
