class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList(Node):
    def __init__(self,value):
        super().__init__(value)
        self.new_node = Node(value)
        self.head = self.new_node
        self.tail = self.new_node
        self.length = 1 if self.new_node else 0

    def append(self,value):
        append_value = Node(value)
        if self.head is None:
            self.head = append_value
            self.tail = append_value
        else:
            self.tail.next = append_value
            self.tail = append_value
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def traverse(self):
        current =self.head
        while current:
            print(current.value)
            current = current.next

ll = LinkedList(2)
ll.append(5)
ll.append(10)
ll.append(11)


print(ll.tail.value)
print(ll)

ll.traverse()