"""
Delete Middle Element of a Linked List

Logic:
    - Loop through the linked list using slow node and fast node. 
    - Keep track of the previous node whenever deleting
    - At the end slow node will be middle.
    - Remove middle element
"""
from LinkedList.singlyLL import SinglyLL


def delete_middle(head):
    """ Delete middle element of a linked list """
    fast_node = head
    slow_node = head
    prev_node = None
    while fast_node and fast_node.next is not None:
        prev_node = slow_node
        slow_node = slow_node.next
        fast_node = fast_node.next.next

    print('Deleting middle element ' + str(slow_node.data))

    prev_node.next = slow_node.next


if __name__ == '__main__':
    ll = SinglyLL()
    for i in range(0, 20):
        ll.append(i)

    print(ll.display())

    delete_middle(ll.head)

    print(ll.display())
