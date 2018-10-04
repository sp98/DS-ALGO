"""
Simple Linear Linked List
"""


class Node:
    """ Node Class """
    def __init__(self, d=None):
        self.data = d
        self.next = None


class SinglyLL:
    """ Simple Liner Linked List Class """
    def __init__(self):
        self.head = None

    def append(self, data):
        """ Append node at the end """
        if not self.head:
            self.head = Node(data)
            return
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    def insert(self, data, index):
        """ Insert node at position """
        if index > self.size():
            print('invalid index')
            return False
        cur_node = self.head
        prev_node = None
        new_node = Node(data)
        cur_index = 0

        while cur_node:
            if cur_index is index:
                prev_node.next = new_node
                new_node.next = cur_node
            prev_node = cur_node
            cur_node = cur_node.next
            cur_index += 1

    def size(self):
        """ find length of the linked list"""
        cur_node = self.head
        total = 0
        while cur_node is not None:
            cur_node = cur_node.next
            total += 1

        return total

    def get_node_at_index(self, index):
        """ Get a node a particular index """
        if index >= self.size():
            print('Invalid index')
            return False

        cur_node = self.head
        cur_pos = 0
        while cur_node.next is not None:
            cur_node = cur_node.next
            if cur_pos == index:
                return cur_node
            cur_pos += 1

    def display(self):
        """ Display the linked list"""
        elem = []
        cur_node = self.head
        while cur_node:
            elem.append(cur_node.data)
            cur_node = cur_node.next
        return elem

    def print_node(self, node):
        """ Print node data """
        if node:
            print(node.data)
        else:
            print(None)
