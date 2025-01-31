class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        temp = self.head
        while temp.next:  # Traverse to the last node
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp  # Link new node with the previous node

    # Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Delete a node by value
    def delete(self, key):
        temp = self.head

        # Case 1: Empty list
        if not temp:
            return

        # Case 2: Delete head node
        if temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        # Case 3: Delete any other node
        while temp and temp.data != key:
            temp = temp.next

        if not temp:  # If key not found
            return

        # Unlink the node
        if temp.next:  # If not the last node
            temp.next.prev = temp.prev
        if temp.prev:  # If not the first node
            temp.prev.next = temp.next

    # Print the list (Forward)
    def print_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Print the list (Backward)
    def print_backward(self):
        temp = self.head
        if not temp:
            return
        while temp.next:
            temp = temp.next  # Move to the last node
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")
