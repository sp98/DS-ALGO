"""
Author: Santosh Pillai
"""


class Node:
    """
    Node class with Data and Next
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    """
    Linked List Class
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Append Node at the end.
        :param data:
        :return:
        """
        if not self.head:
            self.head = Node(data)
            return
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
        while cur_node:
            elem.append(cur_node.data)
            cur_node = cur_node.next

        return elem

    def length(self):
        """
        Display size of the linkedlist
        :return:
        """
        if not self.head:
            return 0

        total = 0
        cur_node = self.head
        while cur_node is not None:
            cur_node = cur_node.next
            total+=1

        return total

    def insert(self, data, index):
        """
        Insert element a particular location.
        :param data:
        :return:
        """
        if index < 0 or index > self.length():
            print("Error: Index value not valid.")
            return

        new_node = Node(data)
            
        cur_node = self.head
        prev_node = None
        cur_index = 0
        while True:
            if cur_index == index:  # insert at first position
                if not prev_node:
                    new_node.next = self.head
                    self.head = new_node
                    return
                else:
                    prev_node.next = new_node
                    new_node.next = cur_node
                    return
            prev_node = cur_node
            cur_node = cur_node.next
            cur_index+=1

    def get(self, index):
        """
        Get data at a particular Index
        :param index:
        :return:
        """
        if index < 0 or index >= self.length():
            return "Error: Invalid Index. Can't be greater than list size or less than 0"

        cur_node = self.head
        cur_index = 0
        while True:
            if cur_index == index:
                return cur_node.data
            cur_node = cur_node.next
            cur_index+=1

    def get_index(self, data):
        """
        Find Index of a particular element
        :param data:
        :return:
        """
        cur_node = self.head
        cur_index = 0
        while cur_node:
            if cur_node.data == data:
                return cur_index
            cur_node = cur_node.next
            cur_index+=1

        return '{} is not present in the list'.format(data)

    def delete_node(self, data):
        """
        Delete a node based on data
        :param data:
        :return:
        """
        cur_node = self.head
        prev_node = None
        while cur_node:
            if cur_node.data == data:
                if not prev_node:
                    self.head = cur_node.next
                    return
                prev_node.next = cur_node.next
                return
            prev_node = cur_node
            cur_node = cur_node.next
            
        return str(data)+ ' is not present in the list.'

    def erase(self, index):
        """
        Delete linkelist node based on index value
        :param index:
        :return:
        """
        if index < 0 or index >= self.length():
            return 'Invalid Index Value'

        cur_node = self.head
        prev_node = None
        cur_index = 0
        while True:
            if cur_index == index:
                if not prev_node:
                    self.head = cur_node.next
                    return
                prev_node.next = cur_node.next
                return
            prev_node = cur_node
            cur_node = cur_node.next
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