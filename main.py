from decorators import do_twice

"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Returning Values From Decorated Functions 
What happens to the return value of decorated functions? Well, that’s up to
the decorator to decide. Let’s say you decorate a simple function as follows

"""


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


# say_whee = my_decorator(say_whee)

if __name__ == "__main__":
    hi_adam = return_greeting("Adam")
    """Because the do_twice_wrapper() doesn’t explicitly return a value, the call return_greeting("Adam") ended up 
    returning None. """
    print(hi_adam)  # Returns None. It only prints
