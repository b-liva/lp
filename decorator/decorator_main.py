from decorators import slow_down

"""
Thanks to: https://realpython.com/primer-on-python-decorators/
Slowing Down Code: example
 """


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


if __name__ == "__main__":
    countdown(3)
