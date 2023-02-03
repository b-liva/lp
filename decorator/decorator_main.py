from decorator.circle import Circle

"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Decorating Classes
There are two different ways you can use decorators on classes. The first one is very close to
what you have already done with functions: you can decorate the methods of a class. This was one of the motivations
for introducing decorators back in the day.

Some commonly used decorators that are even built-ins in Python are @classmethod, @staticmethod, and @property. The
@classmethod and @staticmethod decorators are used to define methods inside a class namespace that are not connected
to a particular instance of that class. The @property decorator is used to customize getters and setters for class
attributes. Expand the box below for an example using these decorators. 
Let’s define a class where we decorate some of its methods using the @debug and @timer decorators from
"""

from decorators import debug, timer


class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(self.max_num)])


if __name__ == "__main__":
    tw = TimeWaster(1000)
    tw.waste_time(999)
