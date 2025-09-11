"""
This implementation is made with the 'queue' library
"""
import queue

orders_queue = queue.SimpleQueue()
orders_queue.put('Andres')
orders_queue.put('Pedro')
orders_queue.put('Maria')

print(f"The size of the queue is: {orders_queue.qsize()}")

print(orders_queue.get())
print(orders_queue.get())
print(orders_queue.get())
#print(orders_queue.get())  ## Infinite loop, doesn't throw any error

print(f"Is the queue empty?: {orders_queue.empty()}")
