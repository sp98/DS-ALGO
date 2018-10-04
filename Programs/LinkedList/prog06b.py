"""
Detect and Remove loop 2
"""

from singlyLL import SinglyLL
from prog01 import insert_node_at


def create_ll_with_loop(ll):
    """ create a sample linked list with loop"""
    index = 4
    for i in range(0, 10):
        insert_node_at(ll.head, i, 0)

    cur_node = ll.head
    while cur_node.next is not None:
        cur_node = cur_node.next

    loop_node = ll.get_node_at_index(index)
    cur_node.next = loop_node


def detect_loop(head):
    """ detect a loop """
    slow_node = head
    fast_node = head
    while fast_node and fast_node.next is not None:
        slow_node = slow_node.next
        fast_node = fast_node.next.next

        if fast_node == slow_node:
            print('Loop Detected')
            return remove_loop(head, slow_node)
    print('No loop detected')
    return False


def remove_loop(head, loop_node):
    """ remove a loop """
    main_node = head

    while True:
        ref_node = loop_node
        while ref_node.next != loop_node and ref_node.next != main_node:
            ref_node = ref_node.next
        if ref_node.next == main_node:
            break

        main_node = main_node.next

    ref_node.next = None


if __name__ == '__main__':
    # Single Linked List
    ll = SinglyLL()
    for i in range(1, 5):
        insert_node_at(ll.head, i, 0)

    detect_loop(ll.head)

    # Single Linked list with loop
    lll = SinglyLL()
    create_ll_with_loop(lll)
    detect_loop(lll.head)

    # after removal of loop
    detect_loop(lll.head)
