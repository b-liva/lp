import math
from decorators import debug

"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Debugging Code 
More useful info.
 """

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


if __name__ == "__main__":
    approximate_e(5)
