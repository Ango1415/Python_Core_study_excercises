# Example of closure for nested functions
def foo():
    a = 5
    def bar():
        print(a)
    return bar

inner_func = foo()
inner_func()
print(type(inner_func.__closure__))
print(len(inner_func.__closure__))
print(f"Value of var 'a' inside foo: {inner_func.__closure__[0].cell_contents}")
print('----------\n')

# Non-local vars are attached to the returned function (nested function)
def parent(arg1, arg2):
    value = 22
    my_dict = {'chocolate': 'yummy'}

    def child():
        print(f"2 times original val: {value * 2}")
        print(f"Value of chocolate: {my_dict['chocolate']}")
        print(arg1 + arg2)

    return child

new_function = parent(3, 4)
"""
Look that we don't need to pass any parameter here, they're already stored in the closure attr of new_function
"""
new_function()
print([cell.cell_contents for cell in new_function.__closure__])
