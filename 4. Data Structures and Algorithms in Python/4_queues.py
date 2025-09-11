"""
They are defined by FIFO "First In First Out"
Can only insert at the end  (Enqueue)
Can only remove from the head
Other types of queues (Doubly ended queues, Circular queues, Priority queues)
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # Enqueue means add a node at the end of the queue
    def enqueue(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    # Dequeue means remove the first node of the queue
    def dequeue(self):
        if self.head:
            current_node = self.head
            self.head = self.head.next
            current_node.next = None
            if self.head is None:
                self.tail = None
            return current_node.data
        else:
            return None

    def print_list(self):
        current_node = self.head
        values = []
        while current_node: # O(n)
            values.append(current_node.data)
            current_node = current_node.next
        print(f"Queue (from head to tail): ({', '.join(map(str, values))})")

queue = Queue()
queue.enqueue('Andres')
queue.enqueue('Pedro')
queue.enqueue('Maria')

queue.print_list()

for _ in range(5):
    print(queue.dequeue())