import time

def timer(func):
    """
    A decorator that prints how long a func took to run.
    Args:
        func (callable): The func being decorated.

    Returns:
        callable: The decorated func.
    """
    # Define the wrapper function to return.
    def wrapper(*args, **kwargs):
        # When the wrapper() is called, get the current time.
        t_start = time.time()
        # Call the decorated func and store the result.
        result = func(*args, **kwargs)
        # Get the total time it took to run, and print it.
        t_total = time.time() - t_start
        print(f"Func '{func.__name__}' took a total of: ''{t_total}'' sec.")
        return result
    return wrapper

@timer
def sleep_n_seconds(n):
        time.sleep(n)

sleep_n_seconds(5)
sleep_n_seconds(10)