def log_decorator(func):
    """
    A decorator that logs the arguments
    and return value of a function.
    """

    def wrapper(*args, **kwargs):
        # Print the name of the function being called and its arguments.
        print(f"Calling {func.__name__} with {args}, {kwargs}")

        # Pass all arguments to the original function ('func').
        # Capture the return value from the original function.
        result = func(*args, **kwargs)

        # Print the value that the original function returned.
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# '@' is the syntax for applying a decorator.
@log_decorator
# The 'add' function will be passed as the 'func' argument to 'log_decorator'.
def add(a, b):
    return a + b

# Execute the decorated function.
add(3, 5)