class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(Node):
    def __init__(self, value):
        super().__init__(value)
        self.new_node = Node(value)
        self.head = self.new_node
        self.tail = self.new_node
        self.length = 0

    def append(self, value):
        # check if linked list is empty
        appended_value = Node(value)
        if self.head is None:
            self.head = appended_value
            self.tail = appended_value
        else:
            self.tail.next = appended_value
            self.tail = appended_value
        self.length += 1

    def prepend(self, value):
        #create a node for the new value to be inserted
        prepend_value = Node(value)
        if self.head is None:
            self.head = prepend_value
            self.tail = prepend_value
        else:
            prepend_value.next = self.head
            self.head = prepend_value
        self.length += 1
        pass

    def insert(self, index, value):
        inserted_value = value
        if index == 0:
            inserted_value.next = self.head
            self.head = inserted_value
        temp_node = self.head
        for _ in range(index-1):
            temp_node = temp_node.next
        inserted_value.next = temp_node.next
        temp_node.next = inserted_value
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

#create a linked list with a single node
new_ll = LinkedList(2)

#append a value to the end of the linked list(tail)
new_ll.append(5)
new_ll.append(10)

# prepend a value at the beginning of the linked list(head)
new_ll.prepend(20)

print(new_ll.head.value)
print(new_ll.tail.value)
print(new_ll.length)

print(new_ll)
