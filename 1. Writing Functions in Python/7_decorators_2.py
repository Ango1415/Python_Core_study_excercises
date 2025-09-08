"""
Let's make an example of how a decorator func can change the behavior of an inner func (or of its params)
This example will work with the explicit use of a decorator
"""
# Decorative func (this func will wrap the above one)
def double_args(func):
    # Define a new func that we can modify
    def wrapper(a, b):
        # Calls the passed func, but double each argument
        return func(a*2, b*2)
    return wrapper

# Original func (this func will be wrapped)
@double_args
def multiply(a, b):
    return a * b

multiply_result = multiply(1,5)
print(multiply_result)
# Look which values are stored in the closure param of our func (Ans: the memory dir of our original func)
print([cell.cell_contents for cell in multiply.__closure__])