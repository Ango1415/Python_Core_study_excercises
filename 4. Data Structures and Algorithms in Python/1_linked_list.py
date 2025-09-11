class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def search(self, data):
        current_node = self.head
        while current_node: # O(n)
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False

    def print_list(self):
        current_node = self.head
        values = []
        while current_node: # O(n)
            values.append(current_node.data)
            current_node = current_node.next
        print(f"Listed link: ({', '.join(map(str, values))})")


sushi = LinkedList()
sushi.insert_at_beginning('prepare')
sushi.insert_at_end('roll')
sushi.insert_at_beginning('assemble')

print(f"Is 'roll' in sushi?: {sushi.search('roll')}")
print(f"Is 'mix' in sushi?: {sushi.search('mix')}")

sushi.print_list()