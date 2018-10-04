''' Doubly linked list '''

class Node:
    def __init__(self, data=None, nxt=None, prev=None):
        self.data = data
        self.nxt = nxt
        self.prev = prev


class Doublyll:
    def __init__(self):
        self.head = None

    def display(self):
        nodes = []
        if not self.head:
            return nodes
        cur_node = self.head
        while cur_node:
            nodes.append(cur_node.data)
            cur_node = cur_node.nxt
        return nodes

    def length(self):
        if not self.head:
            return 0

        total = 0
        cur_node = self.head
        while cur_node:
            total = total + 1
            cur_node = cur_node.nxt
        return total

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return

        cur_node = self.head
        while cur_node:
            if cur_node.nxt is None:
                cur_node.nxt = Node(data, None, cur_node)
                return
            cur_node = cur_node.nxt

    def insert(self, data, index):
        if index < 0 or index >= self.length():
            print('invalid index')
            return

        cur_node = self.head
        prev_node = None
        cur_index = 0
        new_node = Node(data)

        while cur_node:
            if cur_index == index:
                if not prev_node:
                    self.head = Node(data,None, None)
                    return
                # prev_node.nxt = new_node
                # new_node.prev = prev_node
                # new_node.nxt = cur_node
                # cur_node.prev = new_node
                new_node  = Node(data, cur_node, prev_node)
                prev_node.nxt = new_node
                cur_node.prev = new_node
                return

            prev_node = cur_node
            cur_node = cur_node.nxt
            cur_index += 1

    def delete_by_index(self, index):
        if index < 0 or index >= self.length():
            print('invalid index')
            return

        cur_node = self.head
        prev_node = None
        cur_index = 0

        while cur_node:
            if cur_index == index:
                if not prev_node: # deleting at first index
                    self.head = self.head.nxt
                    return
                prev_node.nxt = cur_node.nxt
                cur_node.nxt.prev = prev_node
                return
            prev_node = cur_node
            cur_node = cur_node.nxt
            cur_index += 1

    def delete_by_node(self, data):
        if not self.head:
            print('list is empty')
            return

        cur_node = self.head
        prev_node = None

        while cur_node:
            if cur_node.data == data:
                if not prev_node:  # delete data on first index
                    self.head = self.head.nxt
                    return
                prev_node.nxt = cur_node.nxt
                cur_node.nxt.prev = prev_node
                return
            prev_node = cur_node
            cur_node = cur_node.nxt

        print('node not found')


if __name__ == '__main__':
    dll = Doublyll()
    print(dll.display())
    print(dll.length())

    print('-- Appending --')
    dll.append(4)
    dll.append(8)
    dll.append(-1)
    print(dll.display())

    print(' --inserting --')
    dll.insert(2, 0)
    dll.insert(10, 0)
    print(dll.display())
    dll.insert(11, 3)
    print(dll.display())
    dll.insert(12, 5)
    print(dll.display())

    print('-- deleting by index --')
    dll.delete_by_index(0)
    print(dll.display())
    dll.delete_by_index(1)
    print(dll.display())

    print('-- delete by value --')
    dll.delete_by_node(13)
