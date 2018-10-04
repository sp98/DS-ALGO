"""
Doubly Linked List implementation

"""


class Node:
    """ Node Class """
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLL:
    """ Doubly Linked List class """
    def __init__(self):
        self.head = Node()

    def append(self, data):
        """ Append data into doubly linked list """
        cur_node = self.head
        new_node = Node(data)
        while cur_node.next is not None:
            cur_node = cur_node.next

        cur_node.next = new_node
        new_node.prev = cur_node

    def display(self):
        """ Display The doublly linke list """
        elem = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elem.append(cur_node.data)
        return elem
