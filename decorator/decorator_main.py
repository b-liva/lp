from decorator.decorators import do_twice, debug

"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Nesting Decorators 
You can apply several decorators to a function by stacking them on top of each other Think about 
this as the decorators being executed in the order they are listed. In other words, @debug calls @do_twice, 
which calls greet(), or debug(do_twice(greet())) """


# Equals to debug(do_twice(greet())

@debug
@do_twice
def greet(name):
    print(f"Hello {name}")


@do_twice
@debug
def greet_inverse(name):
    print(f"Hello {name}")


if __name__ == "__main__":
    greet("Eva")
    print("*****************")
    greet_inverse("Eva")
