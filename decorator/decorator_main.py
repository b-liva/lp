from decorators import debug

"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Debugging Code 
The following @debug decorator will print the arguments a function is called with as well as its 
return value every time the function is called """


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


if __name__ == "__main__":
    make_greeting("Benjamin")
    make_greeting("Richard", age=112)
    make_greeting(name="Dorrisile", age=116)
