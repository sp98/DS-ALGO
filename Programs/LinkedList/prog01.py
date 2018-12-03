"""
Insert a node at a specific position in a linked list

"""
from LinkedList.singlyLL import Node, SinglyLL


def insert_node_at(sll, data, position):
    """ Insert data at a posiion
    :param head : Head of the linkelist
    :ptype head : object reference
    :param data : new node to be added
    :ptype data: int
    :param position: index where data has to be added
    :ptype position: int
    :return
    """
    prev_node = None
    cur_node = sll.head
    new_node = Node(data)
    cur_pos = 0

    # invalid index
    if position > sll.size():
        print('Invalid index')
        return False

    # First node
    if cur_node is None:
        print('adding first node')
        cur_node = Node(data)
        return cur_node

    while cur_node is not None:
        if cur_pos == position:
            print('adding new node at pos ' + str(cur_pos))
            prev_node.next = new_node
            new_node.next = cur_node
        prev_node = cur_node
        cur_node = cur_node.next
        cur_pos += 1


if __name__ == '__main__':
    sll = SinglyLL()
    for index, value in enumerate(range(3, 9)):
        insert_node_at(sll, value, 0)
    print(sll.display())
    print(sll.size())
