from decorator.decorators import do_twice, debug, repeat

"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Decorators With Arguments 
Sometimes, it’s useful to pass arguments to your decorators. For instance, @do_twice could 
be extended to a @repeat(num_times) decorator. The number of times to execute the decorated function could then be 
given as an argument 

So far, the name written after the @ has referred to a function object that can be called with another function. To 
be consistent, you then need repeat(num_times=4) to return a function object that can act as a decorator """


# Equals to debug(do_twice(greet())

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")


if __name__ == "__main__":
    greet("World")
