"""
First-Class Objects
In Python, functions are first-class objects. This means that functions can be passed around and used as arguments,
 just like any other object (string, int, float, list, and so on). Consider the following three functions:
"""


def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


if __name__ == "__main__":
    print(say_hello('Robin'))
    print(be_awesome('Jack'))
    print(greet_bob(say_hello))
    print(greet_bob(be_awesome))
