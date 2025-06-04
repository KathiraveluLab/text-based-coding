class deep_dive:
    """This class is well documented but doesn't do anything special."""

    def print_argument(func):
        """This method is a decorator that uses a wrapper to elaborate on the arguments."""
        def wrapper(the_number):
            """This is a wrapper definition."""
            print("Argument for", func.__name__, "is", the_number)
            return func(the_number)
        return wrapper

    @print_argument
    def add_one(x):
        return x + 1

    @print_argument
    def square(x):
        return x * x

    print(add_one(4))
    print(square(3))


help(deep_dive)