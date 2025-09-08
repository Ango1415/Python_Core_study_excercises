# This is an example of a wrapper without params
def run_three_times(func):
    def wrapper(*args, **kwargs):
        for i in range(3): func(*args, **kwargs)
    return wrapper

@run_three_times
def print_sum(a, b):
    print(a + b)

print_sum(3, 5)

"""
To create a decorator who receives a parameter we have to add a new func to the nested functions used before
"""
def run_n_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n): func(*args, **kwargs)

        return wrapper
    return decorator

@run_n_times(3)
def print_mult(a, b):
    print(a * b)

print_mult(3, 5)

"""
We can create a new decorator based on this new parametric decorator
"""
run_four_times = run_n_times(4)

@run_four_times
def print_substr(a, b):
    print(a - b)

print_substr(3, 5)

@run_n_times(5)
def print_hello():
    print('Hello!!')

print_hello()
