# node
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


# The linked list
class LinkedList:
    def _init_(self):
        self.head = None

    # node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # node at start
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # node at position
    def insert_at_index(self, index, data):
        if index < 0:
            raise IndexError("Index cannot be negative.")

        if index == 0:
            self.insert_at_start(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range.")
            current = current.next

        if current is None:
            raise IndexError("Index out of range.")

        new_node.next = current.next
        current.next = new_node

    # Delete node position
    def delete_at_index(self, index):
        if index < 0:
            raise IndexError("Index cannot be negative.")

        if self.head is None:
            raise IndexError("List is empty.")

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of range.")
            current = current.next

        if current.next is None:
            raise IndexError("Index out of range.")

        current.next = current.next.next

    # Search for a value and return its index
    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    # Print all node
    def display(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


