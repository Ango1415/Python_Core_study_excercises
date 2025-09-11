"""
They are defined by LIFO "Last In First Out"
Can only add at the top and can only take from the top
Can only read the last element
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def print_list(self):
        current_node = self.top
        values = []
        while current_node: # O(n)
            values.append(current_node.data)
            current_node = current_node.next
        print(f"Stack (from top to bottom): ({', '.join(map(str, values))})")


my_book_stack = Stack()
my_book_stack.push('The misunderstanding')
my_book_stack.push('Persepolis')
my_book_stack.push('1984')
my_book_stack.print_list()

for _ in range(5):
    print(my_book_stack.pop())