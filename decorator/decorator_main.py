from decorators import decorator

"""
Thanks to: https://realpython.com/primer-on-python-decorators/

A Few Real World Examples Let’s look at a few more useful examples of decorators. You’ll notice that they’ll mainly 
follow the same pattern that you’ve learned so far. """


@decorator
def say_whee():
    print('Whee')


if __name__ == "__main__":
    say_whee()
