"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Inner Functions
It’s possible to define functions inside other functions.
Such functions are called inner functions. Here’s an example of a function with two inner functions
Note that the order in which the inner functions are defined does not matter. Like with any other functions, the printing only happens when the inner functions are executed.

Furthermore, the inner functions are not defined until the parent function is called.
They are locally scoped to parent(): they only exist inside the parent() function as local variables.
Try calling first_child(). You should get an error
Whenever you call parent(), the inner functions first_child() and second_child() are also called. But because of their local scope, they aren’t available outside of the parent() function.
"""


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


if __name__ == "__main__":
    parent()
    first_child()
