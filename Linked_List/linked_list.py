class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(Node):
    def __init__(self, value):
        super().__init__(value)
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

new_node = LinkedList(10)

print(new_node.head.value)