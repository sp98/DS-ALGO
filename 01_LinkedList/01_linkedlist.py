"""
Author: Santosh Pillai
"""


class Node:
    """
    Node class with Data and Next
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """
    Linked List Class
    """
    def __init__(self):
        self.head = Node()

    def append(self, data):
        """
        Append Node at the end.
        :param data:
        :return:
        """
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next

        cur_node.next = Node(data)

    def display(self):
        """
        Display all the elements of the Linked list
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
        Display size of the linkedlist
        :return:
        """
        total = 0
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            total+=1

        return total

    def insert(self, data, index):
        """
        Insert element a particular location.
        :param data:
        :return:
        """
        if index > self.length():
            print("Error: Index value can't be greater than list size.")
            return

        new_node = Node(data)
        cur_node = self.head
        cur_index = 0
        while True:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                prev_node.next = new_node
                new_node.next = cur_node
                return
            cur_index+=1

    def get(self, index):
        """
        Get data at a particular Index
        :param index:
        :return:
        """
        if index >= self.length():
            return "Error: Invalid Index. Can't be greater than the list"

        cur_node = self.head
        cur_index = 0
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index+=1

    def get_index(self, data):
        """
        Find Index of a particular element
        :param data:
        :return:
        """
        cur_node = self.head
        cur_index = 0
        while cur_node.next is not None:
            cur_node = cur_node.next
            if cur_node.data == data:
                return cur_index
            cur_index+=1

        return '{} is not present in the list'.format(data)

    def delete_node(self, data):
        """
        Delete a node based on data
        :param data:
        :return:
        """
        cur_node = self.head
        while cur_node.next is not None:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_node.data == data:
                prev_node.next = cur_node.next
                return self.display()
        return str(data)+ ' is not present in the list.'

    def erase(self, index):
        """
        Delete linkelist node based on index value
        :param index:
        :return:
        """
        if index >= self.length():
            return 'Invalid Index Value'

        cur_node = self.head
        cur_index = 0
        while True:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                prev_node.next = cur_node.next
                return self.display()
            cur_index+=1


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(2)
    linked_list.append(3)
    print(linked_list.display())
    print(linked_list.length())
    linked_list.append(4)
    print(linked_list.display())
    print(linked_list.length())
    linked_list.insert(5,0)
    print(linked_list.display())
    print(linked_list.get(3))
    print(linked_list.get_index(10))
    print(linked_list.delete_node(2))
    print(linked_list.delete_node(10))
    print(linked_list.erase(3))