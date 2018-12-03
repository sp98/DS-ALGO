"""
Detect and remove a loop in a linked list.

Logic:
    - Loop across a linked list and add each
    node into a list.
    - If the node is already present in the list
    then its a loop.
    - Move reference of the previous node to None
"""

from LinkedList.singlyLL import SinglyLL


def create_ll_with_loop(ll):
    """ Create a sample linked list with Loop """
    index = 4
    for i in range(0, 10):
        ll.append(i)

    cur_node = ll.head
    while cur_node.next is not None:
        cur_node = cur_node.next

    loop_node = ll.get_node_at_index(index)
    cur_node.next = loop_node


def detect_remove_loop(head):
    """Detect and remove a loop"""

    cur_node = head
    node_list = []

    while cur_node.next is not None:
        prev_node = cur_node
        cur_node = cur_node.next
        if cur_node not in node_list:
            node_list.append(cur_node)
        else:
            print('Loop Detected')
            prev_node.next = None
            return

    print('No Loop detected')


if __name__ == '__main__':
    ll = SinglyLL()
    for i in range(0, 10):
        ll.append(i)
    print(ll.display())
    detect_remove_loop(ll.head)

    print('Creating a linked list with loop')
    ll2 = SinglyLL()
    create_ll_with_loop(ll2)
    # print('infinite loop')
    # ll2.display()
    print('running LL with loop')

    detect_remove_loop(ll2.head)
    cur_node = ll2.head
    while cur_node is not None:
        print(cur_node.data)
        cur_node = cur_node.next
