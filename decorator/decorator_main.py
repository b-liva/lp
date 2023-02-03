from decorators import timer

"""
Thanks to: https://realpython.com/primer-on-python-decorators/

Timing Functions 
Let’s start by creating a @timer decorator. It will measure the time a function takes to execute and 
print the duration to the console. """


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


if __name__ == "__main__":
    waste_some_time(500)
