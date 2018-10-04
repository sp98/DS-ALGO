"""
Reverse a linked list

Logic:
    1. Loop till the end of the list.
    2. Last item's next value should be head.
    3. Head's next value should None
"""
from singlyLL import SinglyLL

# Head ->  A -> B -> C -> D -> None
# None <-  A <- B <- C <- D <- Head


def reverse_linked_list(ll):
    """ Reverse a linked list """
    prev = None
    cur = ll.head

    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    ll.head = prev


def reverse_linked_list_recursive(head):
    """ Reverse a linked list using recursion """
    if head is None:
        return

    cur_node = head
    next_node = cur_node.next

    if next_node is None:
        print('here')
        return

    next_node = reverse_linked_list_recursive(next_node)
    cur_node.next.next = cur_node
    cur_node.next = None
    print('jere')
    print(cur_node.data)
    return next_node


def reverse_in_groups(head, k):
    """ Reverse a given linked list in groups of K"""
    cur_node = head
    prev_node = None
    next_node = None
    count = 0
    while cur_node and count < k:
        next_node = cur_node.next
        cur_node.next = prev_node
        prev_node = cur_node
        cur_node = next_node
        count += 1

    if next_node is not None:
        head.next = reverse_in_groups(next_node, k)
    
    tt = 'None'
    if head.next:
        tt = head.next.data
    print(str(tt) + ' ---> ' + str(prev_node.data))
    return prev_node


def reverse_in_groups_alt(head, k, is_alt):
    """ Reverse a given lisked list in groups of k, alternatively """
    cur_node = head
    prev_node = None
    next_node = None
    count = 0

    while cur_node and count < k:
        print(cur_node.data)
        next_node = cur_node.next
        if is_alt:
            cur_node.next = prev_node
        prev_node = cur_node
        cur_node = next_node
        count += 1

    if next_node:
        if is_alt:
            is_alt = False
        else:
            is_alt = True
        head.next = reverse_in_groups_alt(next_node, k, is_alt)

    return prev_node


if __name__ == '__main__':
    ll = SinglyLL()
    for i in range(1, 9):
        ll.append(i)
    print(ll.display())
    reverse_linked_list(ll)
    print(ll.display())

    ll2 = SinglyLL()
    for i in range(0, 6):
        ll2.append(i)
    print(ll2.display())
    ll2.head = reverse_linked_list_recursive(ll2.head)
    print(ll2.display())

    print('Reverse every K Node')
    ll3 = SinglyLL()
    for i in range(3, 9):
        ll3.append(i)
    print(ll3.display())
    ll3.head = reverse_in_groups(ll3.head, 2)
    print(ll3.display())

    print('Reverse every K node, alternatively')
    ll4 = SinglyLL()
    for i in range(3, 9):
        ll4.append(i)
    print(ll4.display())
    ll4.head = reverse_in_groups_alt(ll4.head, 2, True)
    print(ll4.display())
