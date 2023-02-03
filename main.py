"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Simple Decorators
Now that you’ve seen that functions are just like any other object in Python, you’re ready to move
on and see the magical beast that is the Python decorator.

In effect, the name say_whee now points to the wrapper() inner function. Remember that you return wrapper as a
function when you call my_decorator(say_whee) However, wrapper() has a reference to the original say_whee() as func,
and calls that function between the two calls to print().
"""


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)

if __name__ == "__main__":
    say_whee()
    print(say_whee)
