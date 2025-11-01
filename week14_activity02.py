import time

def execute_decorator(func):
    """
    A decorator that logs the function call arguments
    and measures its execution time.
    """

    def wrapper(*args, **kwargs):
        # Log the function call (using the raw args/kwargs format as requested)
        print(f"Calling {func.__name__} args={args}, kwargs={kwargs}")
        # Record the start time before execution
        start_time = time.time()
        # Execute the original function, passing *all* captured arguments,
        # both positional (*args) and keyword (**kwargs).
        result = func(*args, **kwargs)

        end_time = time.time()
        elapsed = end_time - start_time
        # Print the total execution time, formatted to 4 decimal places
        print(f"{func.__name__} finished in {elapsed:.4f} seconds.")
        # Return the original function's result
        return result
    # Return the newly defined wrapper function
    return wrapper

# '@' is the syntax for applying a decorator.
@execute_decorator
# The line above is equivalent to:
# time_sleep = execute_decorator(time_sleep)
def time_sleep(sec):
    # Pauses execution for a given number of seconds.
    time.sleep(sec)

# Execute the decorated function.
print("--- Test with positional argument ---")
time_sleep(3)
