from decorator.decorators import timer

"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Decorating Classes
[*] - There are two different ways you can use decorators on classes. The first one is very close to
what you have already done with functions: you can decorate the methods of a class. This was one of the motivations
for introducing decorators back in the day.

Some commonly used decorators that are even built-ins in Python are @classmethod, @staticmethod, and @property. The
@classmethod and @staticmethod decorators are used to define methods inside a class namespace that are not connected
to a particular instance of that class. The @property decorator is used to customize getters and setters for class
attributes. Expand the box below for an example using these decorators. 
Let’s define a class where we decorate some of its methods using the @debug and @timer decorators from

[] - Decorating the whole class

Writing a class decorator is very similar to writing a function decorator. The only difference is that the decorator 
will receive a class and not a function as an argument. In fact, all the decorators you saw above will work as class 
decorators. When you are using them on a class instead of a function, their effect might not be what you want. In the 
following example, the @timer decorator is applied to a class

Here, @timer only measures the time it takes to instantiate the class Later, you will see an example defining a 
proper class decorator, namely @singleton, which ensures that there is only one instance of a class 

 """


@timer
class TimeWaster:  # Equals to TimeWaster = timer(TimeWaster)
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(self.max_num)])


if __name__ == "__main__":
    tw = TimeWaster(1000)
    tw.waste_time(999)
