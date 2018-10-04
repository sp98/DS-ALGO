"""
Reverse a doubly Linked List:
"""

from LinkedList.doublyLL import DoublyLL, Node


def reverse_doubly_ll(dll):
    """ Reverse a doubly linked list """
    head_node = dll.head
    cur_node = dll.head
    cur_node.next.prev = None
    while cur_node.next is not None:
        cur_node = cur_node.next

    cur_node.next = head_node
    head_node.prev = cur_node


if __name__ == '__main__':
    dll = DoublyLL()
    dll.append(3)
    dll.append(4)
    dll.append(5)
    print(dll.display())

    # reverse_doubly_ll(dll)
    # print(dll.display())
