"""
For testing

"""

from singlyLL import SinglyLL


if __name__ == '__main__':
    sll = SinglyLL()

    for i in range(0, 10):
        sll.append(i)

    print(sll.display())
    print(sll.size())
    print(sll.get_node_at_index(12))
    sll.print_node(sll.get_node_at_index(3))
