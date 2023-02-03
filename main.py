"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Returning Functions From Functions
Python also allows you to use functions as return values.
The following example returns one of the inner functions from the outer parent() function

The somewhat cryptic output simply means that the first variable refers to the local first_child() function inside of
parent(), while second points to second_child().

You can now use first and second as if they are regular functions, even though the functions they point to can’t be
accessed directly Finally, note that in the earlier example you executed the inner functions within the parent
function, for instance first_child(). However, in this last example, you did not add parentheses to the inner
functions—first_child—upon returning. That way, you got a reference to each function that you could call in the
future. Make sense?
"""


def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


if __name__ == "__main__":
    first = parent(1)
    second = parent(2)
    print(first)
    print(second)

