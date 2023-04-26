
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class Lista:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Nodo(data)

        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next

    def bubble_sorting(self):
        if self.head is None or self.head.next  is None:
            return
        bubble_list = False
        while not bubble_list:
            bubble_list = True
            current_node = self.head

