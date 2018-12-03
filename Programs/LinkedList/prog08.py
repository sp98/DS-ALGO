"""
Remove duplicate elements from a linkd List
"""

from LinkedList.singlyLL import SinglyLL


def remove_dup(head):
    """ remove duplicates """
    cur_node = head
    node_list = []
    while cur_node.next is not None:
        prev_node = cur_node
        cur_node = cur_node.next
        if cur_node.data in node_list:
            prev_node.next = cur_node.next
        else:
            node_list.append(cur_node.data)


def remove_dup_sorted_list(head):
    """ remove duplicate elements from a sorted list """
    cur_node = head

    while cur_node.next is not None:
        prev_node = cur_node
        cur_node = cur_node.next
        if cur_node.data == prev_node.data:
            prev_node.next = cur_node.next


if __name__ == '__main__':
    print('Removing Dups from an unsorted list')
    sll = SinglyLL()
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(2)
    sll.append(5)
    sll.append(3)

    print(sll.display())

    remove_dup(sll.head)

    print(sll.display())

    print('*' * 10)

    print('Removing dups from a sorted list')

    sll2 = SinglyLL()
    sll2.append(2)
    sll2.append(2)
    sll2.append(3)
    sll2.append(4)
    sll2.append(5)
    sll2.append(6)
    sll2.append(6)

    print(sll2.display())

    remove_dup_sorted_list(sll2.head)

    print(sll2.display())
