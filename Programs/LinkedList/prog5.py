"""
Find nth number from the end of a linked list

Logic 1:
    - Find the length of the linkedlist
    - nth element from the end would be lenth-n+1

Logic 2:
    - Create two pointer for the head.
    - In one loop move first pointer from head to nth element (form the
      beginning)
    - In the second loop move both pointers one by one.
    - When first pointer moves to last item, the second one would be at desired
      location)
"""

from singlyLL import SinglyLL


def find_nth_from_last1(head, pos, length):
    """ Find nth item from the last using length"""
    if pos > length:
        return False

    cur_node = head
    cur_pos = 1
    nth_from_end = length - pos + 1
    while True:
        cur_node = cur_node.next
        if cur_pos == nth_from_end:
            return cur_node.data

        cur_pos += 1

    return cur_node.data


def find_nth_from_last2(head, pos):
    """ Find nth item from the end without length"""
    ref_node = head
    main_node = head
    cur_pos = 1

    while cur_pos is not pos:
        ref_node = ref_node.next
        cur_pos += 1

    while ref_node.next is not None:
        main_node = main_node.next
        ref_node = ref_node.next

    return main_node.data


if __name__ == '__main__':
    sll = SinglyLL()

    for i in range(0, 10):
        sll.append(i)

    print(sll.display())

    print(find_nth_from_last2(sll.head, 2))

    print(find_nth_from_last1(sll.head, 2, sll.size()-1))
