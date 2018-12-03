"""
Find Middle of a linked list in single pass
Logic:
    - Loop through the linked list with two Nodes.
    - One of Nodes increments twice. Other increments once.
    - Once the fast node.next is null, return slow node data
"""

from LinkedList.singlyLL import SinglyLL


def find_middle(head):
    """ Find middle element in a linkedlist """
    slow_node = head
    fast_node = head
    """taking fast_node not none condition to
    prevent nontype error in case of even number
    of nodes.
    """
    while fast_node and fast_node.next is not None:
        slow_node = slow_node.next
        fast_node = fast_node.next.next

    return slow_node.data


if __name__ == '__main__':
    sll = SinglyLL()

    for i in range(0, 10):
        sll.append(i)

    print(sll.display())

    print(find_middle(sll.head))
