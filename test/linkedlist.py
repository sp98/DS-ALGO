''' Linked list '''


class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        cur_node = self.head
        while cur_node:
            nodes.append(str(cur_node.data))
            cur_node = cur_node.nxt

        return '[' + ', '.join(nodes) + ']'

    def append(self, data):

        if not self.head:
            self.head = Node(data=data)
            return

        cur_node = self.head
        while cur_node:
            if cur_node.nxt is None:
                cur_node.nxt = Node(data=data)
                return
            cur_node = cur_node.nxt

    def length(self):
        if not self.head:
            return 0

        total = 0
        cur_node = self.head
        while cur_node is not None:
            total = total + 1
            cur_node = cur_node.nxt

        return total

    def insert(self, data, index):

        if index < 0 or index > self.length():
            print('invalid index')
            return

        cur_node = self.head
        prev_node = None
        cur_index = 0

        while cur_node:
            if cur_index == index:
                if not prev_node:  # to insert data at head
                    self.head = Node(data, cur_node)
                    return
                new_node = Node(data)
                prev_node.nxt = new_node
                new_node.nxt = cur_node
                return
            prev_node = cur_node
            cur_node = cur_node.nxt
            cur_index += 1

    def delete(self, data):
        if not self.head:
            print('linkedlist is empty')
            return

        cur_node = self.head
        prev_node = None
        while cur_node:
            if cur_node.data == data:
                if not prev_node:  # to delete data at head
                    self.head = self.head.nxt
                    return
                prev_node.nxt = cur_node.nxt
                return
            prev_node = cur_node
            cur_node = cur_node.nxt

    # def erase(self, index):
    #     if not self.head:
    #         print('linkedlist is empty')
    #         return
    #     if index < -1 or index > self.length():
    #         print('invalid index')
    #         return
    #
    #     cur_node = self.head
    #     prev_node = None
    #     cur_index = 0
    #     while cur_node.nxt:
    #         if index == cur_index:
    #             if not prev_node:  # delete from head
    #                 self.head = self.head.nxt
    #                 return
    #             prev_node.nxt = cur_node.nxt
    #             return
    #         prev_node = cur_node
    #         cur_node = cur_node.nxt
    #         cur_index += 1

    def get_index(self, data):
        if not self.head:
            print('empty list')
            return

        cur_node = self.head
        cur_index = 0
        while cur_node:
            if cur_node.data == data:
                return cur_index
            cur_node = cur_node.nxt
            cur_index += 1

    def get_node_at_index(self, index):
        if index >= self.length():
            print('invalid index')
            return

        cur_node = self.head
        cur_index = 0
        while cur_node:
            if index == cur_index:
                return cur_node.data
            cur_node = cur_node.nxt
            cur_index += 1


if __name__ == '__main__':
    ll = LinkedList()

    print('-- When linked list is empty --')
    print(ll)
    print(ll.length())

    print('-- After appending items -- ')
    ll.append(5)
    ll.append(6)
    ll.append(8)
    # print(ll)
    # print("Length : ", str(ll.length()))
    # print("Data at index : ", str(ll.get_data(2)))
    # print("Get index of data : ", str(ll.get_index(8)))

    # print('-- Inserting at index -- ')
    # ll.insert(10, 100)
    # print(ll)
    # ll.insert(10, 1)
    # print(ll)
    # ll.insert(11, 0)
    # print(ll)
    # ll.insert(100, ll.length())
    print(ll)

    print(ll.get_node_at_index(ll.length()-1))
    print(ll.get_index(8))

    # ll.delete(11)
    # print(ll)
    # ll.erase(ll.length())
    # print(ll)
    # ll.erase(0)
    # print(ll)

