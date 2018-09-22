"""
Author: Santosh Pillai
Email: santosh.pillai98@gmail.com

"""


class Node:
    """
    Node class with data, next and previous
    """
    def __init__(self, data=None):
        """
        Initialize
        :param data:
        """
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    """
    Doubly Linked List Class
    """
    def __init__(self):
        self.head = Node()

    def append(self, data):
        """
        Append data at end of doubly linked list
        :param data:
        :return:
        """
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next

        cur_node.next = new_node
        new_node.previous = cur_node

    def display(self):
        """
        Display doubly linkeed list data
        :return:
        """
        elem = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elem.append(cur_node.data)

        return elem

    def length(self):
        """
        Length of double linked list
        """
        total = 0
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            total+=1
        return total

    def insert(self, data, index):
        """
        Insert a data at an index in DLL
        :param data:
        :return:
        """
        if index >= self.length():
            return '{} is an invalid index.'.format(index)

        new_node = Node(data)
        cur_node = self.head
        cur_index = 0
        while True:
            #prev_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                # prev_node.next = new_node
                # new_node.previous = prev_node
                # new_node.next = cur_node
                # cur_node.previous = new_node
                cur_node.previous.next = new_node
                new_node.previous = cur_node.previous
                new_node.next = cur_node.next
                cur_node.next.previous = new_node
                return self.display()

    def erase(self, index):
        """
        delete node at an index
        :param data:
        :param index:
        :return:
        """
        if index >= self.length():
            return '{} is an invalid index'.format(index)

        cur_node = self.head
        cur_index = 0
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                cur_node.previous.next = cur_node.next
                cur_node.next.previous = cur_node.previous
                return self.display()
            cur_index+=1

    def delete_node(self, data):
        """
        Remove node on an index
        :param index:
        :return:
        """
        cur_node = self.head
        if cur_node.next is None:
            return 'Delete operation not valid on empty list'
        while True:
            cur_node = cur_node.next
            if cur_node.data == data:
                cur_node.previous.next = cur_node.next
                cur_node.next.previous = cur_node.previous
                return self.display()
        return '{} not found in the list'.format(data)


    def sample(self):
        cur_node = self.head
        print(cur_node.data)
        print(cur_node.next.data)
        print(cur_node.next.next.data)
        print(cur_node.next.next.next.data)
        print(cur_node.next.next.next.previous.previous.data)
        print(self.display())


if __name__ == '__main__':
    dll = DoublyLinkedList()
    print(dll.delete_node(2))
    print(dll.erase(0))
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    # print(dll.display())
    # print(dll.insert(4, 0))
    # print(dll.length())
    # print(dll.erase(0))
    # print(dll.delete_node(2))
    # print(dll.display())
    print('**' * 10)
    print(dll.display())
    print(dll.delete_node(2))
    dll.sample()
