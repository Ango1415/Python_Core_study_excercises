"""
This implementation is made with the 'queue' library
"""
import queue

my_book_stack = queue.LifoQueue()
my_book_stack.put('The misunderstanding')
my_book_stack.put('Persepolis')
my_book_stack.put('1984')

print(f"The size of the stack is: {my_book_stack.qsize()}")

print(my_book_stack.get())
print(my_book_stack.get())
print(my_book_stack.get())
#print(my_book_stack.get()) # Infinite loop, doesn't throw any error

print(f"The stack is empty?: {my_book_stack.empty()}")