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
attributes. Expand the box below for an example using these decorators. """

if __name__ == "__main__":
    c = Circle(5)
    print(c.radius)
    print(c.area)
    c.radius = 2
    print(c.area)
    # c.area = 4 # This can not be done.
    print(c.cylinder_volume(height=4))
    c = Circle.unit_circle()
    print(c.radius)
    print(c.pi())
    print(Circle.pi())
    c.radius = -1
