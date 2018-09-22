"""
Author: Santosh Pillai
Email: santosh.pillai98@gmial.com
"""


class Node:
    """ Linked List Node """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    """ Circular Linked List Implementation """
    def __init__(self):
        self.head = Node()
        self.head.next = self.head

    def append(self, data):
        """
        Append a data to the Circular Linked List
        :param data:
        :return:
        """
        cur_node = self.head
        while cur_node.next is not self.head:
            cur_node = cur_node.next

        new_node = Node(data, cur_node.next)
        cur_node.next = new_node
        return self.display()

    def display(self):
        """
        Display Circular Linked List data
        :return:
        """
        elem = []
        cur_node = self.head
        while cur_node.next is not self.head:
            cur_node = cur_node.next
            elem.append(cur_node.data)
        return elem

    def length(self):
        """
        find length of the circualr linked list
        :return:
        """
        total= 0
        cur_node = self.head
        while cur_node.next is not self.head:
            cur_node = cur_node.next
            total+=1

        return total

    def insert(self, data, index):
        """
        Insert new node a particular index
        :param data:
        :param index:
        :return:
        """
        if index >= self.length():
            return '{} index is not valid.'.format(index)
        cur_node = self.head
        cur_index = 0
        while cur_node.next is not self.head:
            cur_node = cur_node.next
            if cur_index == index:
                print('adding ' + str(data) + ' between ' + str(cur_node.data)
                      + ' and ' + str(cur_node.next.data))
                new_node = Node(data, cur_node.next)
                cur_node.next = new_node
            cur_index+=1
        return self.display()

    def delete(self, data):
        """
        Delete node from CLL based on the data
        :param data:
        :return:
        """
        cur_node = self.head
        while cur_node.next is not self.head:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_node.data == data:
                print('Deleting ' + str(data) + ' between ' + str(prev_node.data)
                      + ' and ' + str(cur_node.data))
                prev_node.next = cur_node.next
                return self.display()
        return '{} not found in the CLL'.format(data)

    def erase(self, index):
        """
        Delete node based on index value
        :param index:
        :return:
        """
        if index >= self.length():
            return '{} invalid index value'.format(index)

        cur_node = self.head
        cur_index = 0
        while cur_node.next is not self.head:
            prev_node = cur_node
            cur_node = cur_node.next
            if index == cur_index:
                print('Deleting between ' + str(prev_node.data)
                    + ' and ' + str(cur_node.next.data))
                prev_node.next = cur_node.next
                return self.display()
            cur_index+=1


    def test(self):
        """
        Testing the implementation
        :return:
        """
        print('----- Testing CLL -----')
        print('--current--')
        print(self.display())
        cur_node = self.head
        while cur_node.next is not self.head:
            print(cur_node.data)
            cur_node = cur_node.next
        print('--- checking circular ---')
        print(cur_node.data)
        print(cur_node.next.data)
        print(cur_node.next.next.data)
        print('--- Test  Completed ---')


if __name__ == '__main__':
    cll = CircularLinkedList()
    #print(cll.head.data)
    print(cll.append(1))
    print(cll.append(2))
    print(cll.append(3))
    print(cll.display())
    print(cll.length())
    #print(cll.test())
    print(cll.insert(4,1))
    print(cll.insert(5, cll.length()-1))
    print(cll.delete(1))
    print(cll.erase(0))
    #print(cll.test())




