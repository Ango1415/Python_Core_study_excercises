# Factorial without recursion
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)


print(factorial(5))
print(factorial_recursive(5))